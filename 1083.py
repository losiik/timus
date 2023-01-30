factor = input()

data = factor.split()
numb = int(data[0])
k = len(data[1])

result = 1
mod_n = numb % k
if mod_n == 0:
    while True:
        result *= numb
        if numb == k:
            break
        numb -= k
else:
    while True:
        result *= numb
        if numb == mod_n:
            break
        numb -= k


print(result)
