from sys import argv

l1 = open(argv[1] + ".sent").readlines()
l2 = open(argv[1] + ".tuple").readlines()
l3 = open(argv[1] + ".pointer").readlines()

assert len(l1) == len(l2) and len(l2) == len(l3)

final1 = []
final2 = []
final3 = []

for i in range(len(l1)):
    if len(l2[i]) == 1:
        assert len(l2[i]) == len(l3[i])
    else:
        final1.append(l1[i])
        final2.append(l2[i])
        final3.append(l3[i])


open(argv[1] + ".sent", "w").writelines(final1)
open(argv[1] + ".tuple", "w").writelines(final2)
open(argv[1] + ".pointer", "w").writelines(final3)

print("Old:", len(l1), "New:", len(final1))