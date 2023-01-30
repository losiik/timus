n = int(input())
counter = 2

for i in range(n):
  name = input()
  counter += 1
  for j in range(len(name)):
    if (name[j] == '+'):
      counter += 1

if (counter == 13):
  counter += 1

print(counter*100)
