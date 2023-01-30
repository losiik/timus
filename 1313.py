n = int(input())
a = []

for i in range(n):
  temp = input()
  temp = temp.split()
  a.append(temp)

for i in range(0, n):
  for j in range(0, i + 1):
    print(a[i-j][j], end = ' ')

for i in range(n, 2*n):
  for j in range(n - 1, i - n, -1):
    print(a[j][i - j], end = ' ')