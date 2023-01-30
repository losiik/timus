a_b = input()

a_b = a_b.split()
S = int(a_b[0]) * int(a_b[1])

if S % 2 == 0:
    print('[:=[first]')
else:
    print('[second]=:]')