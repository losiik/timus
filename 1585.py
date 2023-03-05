n = int(input())

emperor_penguins_counter = 0
little_penguins = 0
macaroni_penguins = 0

for i in range(n):
    penguin = input()
    if penguin == 'Emperor Penguin':
        emperor_penguins_counter += 1
    elif penguin == 'Macaroni Penguin':
        macaroni_penguins += 1
    else:
        little_penguins += 1

max_penguins = max(emperor_penguins_counter, little_penguins, macaroni_penguins)
if max_penguins == emperor_penguins_counter:
    print('Emperor Penguin')
elif max_penguins == little_penguins:
    print('Little Penguin')
else:
    print('Macaroni Penguin')