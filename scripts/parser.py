from __future__ import print_function

import os
from sys import argv, exit, stderr
import xml.etree.ElementTree as ET
from pprint import pprint
from copy import deepcopy


def sent_parser(root: ET.Element):
    words = [w.text.strip() for w in root.findall(".//W")]
    words = ["[unused 1]", "[unused 2]"] + words

    print(" ".join(words))


def tuple_parser(root: ET.Element):
    events = {}
    for tag in root.iter():
        if tag.tag.endswith("_EVENT"):
            phrase = [w.text.strip() for w in tag.findall(".//W")]
            if len(phrase) == 0:
                continue
            events[tag.attrib["ID"]] = {
                "id": tag.attrib["ID"],
                "name": tag.tag,
                "type": tag.attrib["TYPE"],
                "phrase": " ".join(phrase),
                "found_arg": False
            }

    event_args = []
    for tag in root.iter():
        if tag.tag.endswith("-ARG"):
            try:
                phrase = [w.text.strip() for w in tag.findall(".//W")]
                if len(phrase) == 0:
                    continue
                event_id = tag.find("./LINK").get("EVENT_ARG")
                ev_arg = (
                    events[event_id]["phrase"],
                    events[event_id]["name"] + ":" + events[event_id]["type"],
                    " ".join(phrase),
                    tag.tag
                )
                event_args.append(ev_arg)
                events[event_id]["found_arg"] = True
            except:
                ev_arg = (
                    "[unused 1]",
                    "[unused 1]",
                    " ".join(phrase),
                    tag.tag
                )
                event_args.append(ev_arg)

    for v in events.values():
        if not v["found_arg"]:
            ev_arg = (
                v["phrase"],
                v["name"] + ":" + v["type"],
                "[unused 2]",
                "[unused 2]"
            )
            event_args.append(ev_arg)

    print("|".join([";".join(w) for w in event_args]))


def pointer_parser(root: ET.Element):
    # First 2 tokens are [unused 1] and [unused 2]
    cnt = 0
    for w in root.findall(".//W"):
        w.set("count", cnt + 2)
        cnt += 1

    events = {}
    for tag in root.iter():
        if tag.tag.endswith("_EVENT"):
            idxs = [w.attrib["count"] for w in tag.findall(".//W")]
            if len(idxs) == 0:
                continue
            events[tag.attrib["ID"]] = {
                "id": tag.attrib["ID"],
                "name": tag.tag,
                "type": tag.attrib["TYPE"],
                "start": str(min(idxs)),
                "end": str(max(idxs)),
                "found_arg": False
            }

    event_args = []
    for tag in root.iter():
        if tag.tag.endswith("-ARG"):
            try:
                idxs = [w.attrib["count"] for w in tag.findall(".//W")]
                if len(idxs) == 0:
                    continue
                event_id = tag.find("./LINK").get("EVENT_ARG")
                ev_arg = (
                    events[event_id]["start"], events[event_id]["end"],
                    events[event_id]["name"] + ":" + events[event_id]["type"],
                    str(min(idxs)), str(max(idxs)),
                    tag.tag
                )
                event_args.append(ev_arg)
                events[event_id]["found_arg"] = True
            except:
                ev_arg = (
                    "0", "0",
                    "[unused 1]",
                    str(min(idxs)), str(max(idxs)),
                    tag.tag
                )
                event_args.append(ev_arg)

    for v in events.values():
        if not v["found_arg"]:
            ev_arg = (
                v["start"], v["end"],
                v["name"] + ":" + v["type"],
                "1", "1",
                "[unused 2]"
            )
            event_args.append(ev_arg)

    print("|".join([";".join(w) for w in event_args]))

# Structure:
#    Document -> P -> W
# OR Document -> P -> ARG/Event -> W
def break_p(root:ET.Element, delim):
    p_cnt = 0
    for p in root.findall(".//P"):
        for w in p.findall(".//W"):
            w.set("P_CNT", p_cnt)
            if delim in w.text:
                p_cnt += 1
        p_cnt += 1

    ps = root.findall(".//P")
    ps_final = {}

    for p in ps:
        pc = set()
        for w in p.findall(".//W"):
            pc.add(w.get("P_CNT"))
        
        for c in pc:
            ps_final[c] = deepcopy(p)
    
    for k, v in ps_final.items():
        for w in v.findall(".//W"):
            if w.get("P_CNT") != k:
                for el in v.iter():
                    if w in el:
                        el.remove(w)

    return list(ps_final.values())    

if __name__ == "__main__":
    if len(argv) not in [2, 3]:
        print("Usage: python3 parser.py (mode:sent|tuple|pointer) [directory]")
        exit(-1)

    if len(argv) == 2:
        directory = "../data"
    else:
        directory = argv[2]

    mode = argv[1]

    all_files = []

    all_text_files = []

    for root, _, files in os.walk(directory):
        for name in files:
            if os.path.splitext(name)[1] == ".xml":
                all_files.append(os.path.join(root, name))
            else:
                all_text_files.append(os.path.join(root, name))

    for name in all_text_files:
        try:
            all_files.index(os.path.splitext(name)[0] + ".xml")
        except Exception as e:
            print(e, file=stderr)

    print("Total", len(all_files), "files detected", file=stderr)

    for fname in all_files:
        tree = ET.parse(fname)
        root = tree.getroot()

        for p in break_p(root, '???'):
            if mode == "sent":
                sent_parser(p)
            elif mode == "tuple":
                tuple_parser(p)
            elif mode == "pointer":
                pointer_parser(p)
            else:
                print("Garbage mode", file=stderr)
