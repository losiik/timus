n = int(input())
buffer = input()
buffer = buffer.split()
seq = []
counter = 1

for i in range(1, n):
  if buffer[i - 1] == buffer[i]:
    counter += 1
  else:
    seq.append(counter)
    seq.append(buffer[i - 1])
    counter = 1

seq.append(counter)
seq.append(buffer[len(buffer) - 1])

for i in range(len(seq)):
  print(seq[i], end=' ')