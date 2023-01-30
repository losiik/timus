a, b = map(int, input().split())
arr = input()
arr = arr.split()

i = 0
j = 0
t = ' '

rows = a//b
if a % b > 0:
  rows += 1

if a == b:
  step = 1
else:
  step = rows

for l in range(a):
  if len(arr[l]) < 4:
    arr[l] = t * (4 - len(arr[l])) + arr[l]

while j < rows:
  i = j
  while i <= a - 1:
      print(arr[i], end = '')
      i += step
  print(end = '\n')
  j += 1