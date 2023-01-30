cpm, mins = map(int, input().split())
string = input().split()

cars = 0
for i in range(len(string)):
  cars += int(string[i]) - cpm
  if cars < 0:
    cars = 0

print(cars)