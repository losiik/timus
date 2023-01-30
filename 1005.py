from itertools import combinations

n = int(input())
weight = input()
weight = weight.split()

total_weight = 0
half_weight = 0
best_comb = 0

for i in range(len(weight)):
    weight[i] = int(weight[i])
    total_weight += weight[i]

half_weight = total_weight / 2

min_weight_difference = half_weight
all_combinations = [sum(x) for n in range(len(weight)) for x in combinations(weight, n + 1)]

for combo in all_combinations:
    if abs(half_weight - combo) < min_weight_difference:
        min_weight_difference = abs(half_weight - combo)
        best_comb = combo

print(abs(total_weight - best_comb*2))

