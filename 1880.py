n1 = int(input())
numbs1 = input().split()
n2 = int(input())
numbs2 = input().split()
n3 = int(input())
numbs3 = input().split()

counter = 0

for i in range(n1):
  if (numbs1[i] in numbs2) and (numbs1[i] in numbs3):
    counter += 1

print(counter)