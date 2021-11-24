from sys import argv

fname = argv[1]

event_max = -1
arg_max = -1

with open(fname, "r") as f:
    lines = f.readlines()
    for l in lines:
        l = l.strip()
        parts = l.split("|")
        for p in parts:
            arr = p.split(";")
            ev = int(arr[1]) - int(arr[0]) + 1
            ar = int(arr[4]) - int(arr[3]) + 1
            if event_max < ev:
                event_max = ev
            if arg_max < ar:
                arg_max = ar

print(fname, "Event:", event_max, "Arg:", arg_max)
