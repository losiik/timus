import math
l, h, w = map(int, input().split())

l = l / 100
h = h / 100
if h <= l / 2:
  print("butter")
else:
  t = math.sqrt((h - l / 2) / 9.81 * 2)
  turn = t * w / 60
  if (turn % 1 > 0 and turn % 1 < 0.25) or turn % 1 > 0.75:
    print("butter")
  else:
    print("bread")