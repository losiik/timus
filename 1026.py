n = int(input())
database = []
request = []

def count_sorting(database, n):
  maximum = max(database)
  minimum = min(database)
  len_help_arr = maximum - minimum + 1
  help_arr = [0]*len_help_arr

  for i in range(n):
    help_arr[database[i] - minimum] += 1

  index = 0
  for i in range(len(help_arr)):
    for j in range(help_arr[i]):
      database[index] = i + minimum
      index += 1

for i in range(n):
  database.append(int(input()))

count_sorting(database, n)

markline = input()
n = int(input())

for i in range(n):
  request.append(int(input()))

for i in range(n):
  print(database[request[i] - 1])