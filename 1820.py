import math

n, k = map(int, input().split())

if n > k:
  print(math.ceil(n * 2 / k))
else:
  print(2)