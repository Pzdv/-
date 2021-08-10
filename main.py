def make_combination(combination: [], elements_left, position):
    if elements_left == 0:
        combinations.append(combination.copy())
        return
    if position == len(combination):
        return

    combination[position] = True
    make_combination(combination, elements_left - 1, position + 1)
    combination[position] = False
    make_combination(combination, elements_left, position + 1)


combinations = []
all_numbs_combinations = []
result = []
n, k = [int(x) for x in input().split()]
input_array = [int(x) for x in input().split()]

make_combination([False] * (n - 1), k, 0)

for e in range(0, len(input_array)):
    partial_array = tuple([input_array[x] for x in range(0, len(input_array)) if e != x])
    e_number = input_array[e]

    numbs_combination = []
    for comb in combinations:
        for x in range(0, len(comb)):
            if comb[x]:
                numbs_combination.append(partial_array[x])
        all_numbs_combinations.append(tuple(numbs_combination))
        numbs_combination.clear()

    min_distance = -1
    for comb in all_numbs_combinations:
        current_distance = 0
        for x in comb:
            current_distance += abs(e_number-x)
        if min_distance == -1:
            min_distance = current_distance
        if min_distance > current_distance:
            min_distance = current_distance

    result.append(min_distance)
    all_numbs_combinations.clear()

for x in result:
    print(x)
