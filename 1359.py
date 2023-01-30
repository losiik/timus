from math import sqrt, inf

n, m = map(int, input().split())

time_list = []
for i in range(n+1):
    time_list.append([])
    for j in range(m+1):
        time_list[-1].append(inf)

time_list[0][0] = 0

v = [0]
for i in range(1, m+1):
    v.append(sqrt(2*10*i))


def min_time():
    sin = (y_end - y_start) / sqrt((x_end - x_start)**2 + (y_end - y_start)**2)
    time_list[x_end][y_end] = min(time_list[x_end][y_end], time_list[x_start][y_start] + abs(v[y_end]-v[y_start])/(10*sin))


for y_end in range(1, m + 1):
    for x_end in range(0, n + 1):
        for y_start in range(0, y_end):
            for x_start in range(0, x_end + 1):
                min_time()

print(time_list[n][m])