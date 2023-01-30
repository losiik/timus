a = int(input())
b = int(input())
c = int(input())

max_numb = max(a, b, c)
min_numb = min(a, b, c)

sum_numb = a + b + c

first_res = min_numb - (sum_numb - max_numb - min_numb) * max_numb
second_res = min_numb - (sum_numb - max_numb - min_numb) - max_numb

if second_res > first_res:
    print(first_res)
else:
    print(second_res)


