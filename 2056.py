n = int(input())
a = []

for i in range(n):
  a.append(int(input()))

for i in range(n):
  if a[i] == 3:
    print("None")
    exit(0)

if (sum(a) / n == 5):
  print("Named")
elif (sum(a) / n >= 4.5):
  print("High")
else:
  print("Common")