from __future__ import print_function

import os
from sys import argv, exit, stderr
import xml.etree.ElementTree as ET

n_event = 0
n_arg = 0
len_event = 0
len_arg = 0

def count_event_arg(root: ET.Element):
    global n_arg, n_event, len_arg, len_event

    cnt = 0
    for w in root.findall(".//W"):
        w.set("count", cnt)
        cnt += 1

    for tag in root.iter():
        if tag.tag.endswith("_EVENT"):
            n_event += 1
            idxs = [w.attrib["count"] for w in tag.findall(".//W")]
            len_event += len(idxs)

    event_args = []
    for tag in root.iter():
        if tag.tag.endswith("-ARG"):
            idxs = [w.attrib["count"] for w in tag.findall(".//W")]
            len_arg += len(idxs)
            n_arg += 1
                

if __name__ == "__main__":
    directory = argv[1]
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
        count_event_arg(root)

    print("Total Event:", n_event)
    print("Avg Event Length:", len_event / n_event)
    print("Total Arg:", n_arg)
    print("Avg Arg Length:", len_arg / n_arg)