n = int(input())
n -= 2
flag1 = flag2 = 1

while n > 0:
    flag1, flag2 = flag2, flag1 + flag2
    n -= 1

print(flag2 * 2)