n = int(input())
counter = 0
simple_numb = 2
buffer = 0


def increase():
    global simple_numb
    simple_numb += 2
    if simple(simple_numb) == True:
        return
    else:
        increase()


def simple(n):
    global buffer
    if n % 1 > 0:
        return False
    elif n % 2 == 0:
        return n == 2
    if buffer > 3:
        d = buffer
    else:
        d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


while simple_numb * simple_numb <= n:
    if counter > 20 or simple_numb ** (20 - counter) > n:
        break
    elif (20 - counter > 0 and n ** (1 / (20 - counter)) == simple_numb) or (
            20 - counter > 0 and simple(n ** (1 / (20 - counter))) == True):
        counter = 20
        break
    elif n % simple_numb == 0:
        n = n // simple_numb
        counter += 1
        if simple(n) == True:
            counter += 1
            break
    else:
        if simple_numb > 2:
            increase()
        else:
            simple_numb += 1
        buffer = simple_numb

if counter == 20:
    print("Yes")
else:
    print("No")