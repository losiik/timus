n = int(input())
magic_fields = input()

magic_fields = magic_fields.split()
magic_fields = list(map(int, magic_fields))

# sum_fields: position
output_values = {}

field_temp = magic_fields[0]
counter = 1
sum_fields = field_temp

for i in range(1, len(magic_fields)):
    if magic_fields[i] == field_temp:
        counter += 1
        sum_fields += field_temp
    else:
        counter = 1
        field_temp = magic_fields[i]
        sum_fields = field_temp

    if counter == 3:
        output_values[sum_fields] = i

max_key = max(list(output_values))
print(max_key, output_values[max_key])