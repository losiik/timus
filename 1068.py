n = int(input())
s = 0

if n > 0:
  i = 1
else:
  i = -1

for k in range(1, n + i, i):
  s += k

print(s)