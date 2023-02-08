n = int(input())

i = 0
j = 0
while i < n:
    if j % 2 == 1:
        result = 'black'
    else:
        result = 'grimy'
    i += 2
    j += 1

print(result)

'''
1 нечет
1 2 нечет
1 2 3 чет
1 2 3 4 чет
1 2 3 4 5 нечет
1 2 3 4 5 6 нечет
1 2 3 4 5 6 7 чет
'''