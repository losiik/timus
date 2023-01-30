n = int(input())

fields = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ['1', '2', '3', '4', '5', '6', '7', '8']]


for i in range(n):
    position = input()
    letter_p = position[0]
    numb_p = position[1]
    
    attacked_fields = []
    letter_p_index = fields[0].index(letter_p)
    numb_p_index = fields[1].index(numb_p)

    try:
        attacked_fields.append(fields[0][letter_p_index + 2] + fields[1][numb_p_index + 1])
    except:
        pass
    try:
        if numb_p_index - 1 >= 0:
            attacked_fields.append(fields[0][letter_p_index + 2] + fields[1][numb_p_index - 1])
    except:
        pass
    try:
        if letter_p_index - 2 >= 0:
            attacked_fields.append(fields[0][letter_p_index - 2] + fields[1][numb_p_index + 1])
    except:
        pass
    try:
        if letter_p_index - 2 >= 0 and numb_p_index - 1 >= 0:
            attacked_fields.append(fields[0][letter_p_index - 2] + fields[1][numb_p_index - 1])
    except:
        pass
    try:
        if fields[1][numb_p_index + 2] + fields[0][letter_p_index + 1] not in attacked_fields:
            attacked_fields.append(fields[1][numb_p_index + 2] + fields[0][letter_p_index + 1])
    except:
        pass
    try:
        if fields[1][numb_p_index + 2] + fields[0][letter_p_index - 1] not in attacked_fields and letter_p_index - 1 >= 0:
            attacked_fields.append(fields[1][numb_p_index + 2] + fields[0][letter_p_index - 1])
    except:
        pass
    try:
        if fields[1][numb_p_index - 2] + fields[0][letter_p_index + 1] not in attacked_fields and numb_p_index - 2 >= 0:
            attacked_fields.append(fields[1][numb_p_index - 2] + fields[0][letter_p_index + 1])
    except:
        pass
    try:
        if fields[1][numb_p_index - 2] + fields[0][letter_p_index - 1] not in attacked_fields and numb_p_index - 2 >=0 and letter_p_index - 1 >= 0:
            attacked_fields.append(fields[1][numb_p_index - 2] + fields[0][letter_p_index - 1])
    except:
        pass

    print(len(attacked_fields))
