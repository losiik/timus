n = int(input())
magic_fields = input()

magic_fields = magic_fields.split()
magic_fields = list(map(int, magic_fields))

result = 0
pos = 0
final_result = 0

for i in range(n - 2):
    result += magic_fields[i] + magic_fields[i + 1] + magic_fields[i + 2]
    if result > final_result:
        final_result = result
        pos = i + 2
    result = 0

print(final_result, pos)