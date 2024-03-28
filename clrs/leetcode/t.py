import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    a = line.split(",")
    a.sort()
    print(",".join(a))
