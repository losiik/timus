n = int(input())
numbs = ""
div = 9
N = n


def convert():
    global N, n, numbs, div
    if N > 0 and N < 10:
        return N
    if n == 0:
        return 10
    elif n % div == 0:
        n = n // div
        numbs = str(div) + numbs
        if n > 0 and n < 10:
            numbs = str(n) + numbs
            return numbs
        else:
            return convert()
    else:
        div -= 1
        if div == 1:
            return -1
        else:
            return convert()


print(convert())