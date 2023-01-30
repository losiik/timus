import math

N, R = map(float, input().split())
N = int(N)
x = [0 for i in range(N)]
y = [0 for i in range(N)]
thread_length = 0

def straight_length(x1, x2, y1, y2):
  return math.sqrt((abs(x1-x2))**2 + (abs(y1-y2))**2)

for i in range(N):
  x[i], y[i] = map(float, input().split())

for i in range(N - 1):
  thread_length += straight_length(x[i], x[i+1], y[i], y[i+1])

thread_length += straight_length(x[N-1], x[0], y[N-1], y[0]) + 2 * 3.14 * R

print(round(thread_length, 2))