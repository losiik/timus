from sys import stdin
import math

lines = []
for line in stdin:
    line = line.split()
    for l in line:
        lines.append(math.sqrt(int(l.rstrip('\n'))))


for line in reversed(lines):
    print(f"{line:.5f}")


