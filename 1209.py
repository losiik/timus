import math

n = int(input())

answer = []

for i in range(n):
    pos = int(input())
    if math.sqrt(8*pos - 7) % 1 == 0:
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))
