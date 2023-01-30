n = int(input())
groups = input().split()

def sorting():
  global groups

  for i in range(len(groups) - 1):
    for j in range(i+1, len(groups)):
      if int(groups[i]) > int(groups[j]):
        temp = groups[i]
        groups[i] = groups[j]
        groups[j] = temp

def main_part(n):
  if n / 2 % 1 > 0:
    return int(n / 2) + 1
  return n / 2 + 1

def count():
  global groups
  half = main_part(len(groups))
  counter = 0

  for i in range(half):
    counter += main_part(int(groups[i]))

  return counter

sorting()
print(count())