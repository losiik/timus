rub_dict = {1: ['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y', '.', ' '],
            2: ['b', 'e', 'h', 'k', 'n', 'q', 't', 'w', 'z', ','],
            3: ['c', 'f', 'i', 'l', 'o', 'r', 'u', 'x', '!']}
counter = 0

message = input()

for letter in message:
    for key in list(rub_dict.keys()):
        if letter in rub_dict[key]:
            counter += key
            break

print(counter)