import sys

fname = sys.argv[1]

with open(fname, "r") as f:
    lines = f.readlines()
    wc = [len(a.split()) - 2 for a in lines]
    print(max(wc))
