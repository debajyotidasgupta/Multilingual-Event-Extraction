from __future__ import print_function

import os
from sys import argv, exit, stderr
import xml.etree.ElementTree as ET
from pprint import pprint


def sent_parser(root: ET.Element):
    words = [w.text.strip() for w in root.findall(".//W")]
    words = ["[unused 1]", "[unused 2]"] + words

    print(" ".join(words))


def tuple_parser(root: ET.Element):
    pass

def pointer_parser(root: ET.Element):
    pass


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

        if mode == "sent":
            sent_parser(root)
        elif mode == "tuple":
            tuple_parser(root)
        elif mode == "pointer":
            pointer_parser(root)
        else:
            print("Garbage mode", file=stderr)
