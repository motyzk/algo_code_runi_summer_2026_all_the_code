def solve(values, weights, limit):
    table = [[0 for _ in range(limit + 1)]]
    for j in range(1, len(values) + 1):
        curr_item_max_values = [0]
        for w in range(1, limit + 1):
            if weights[j-1] > w:
                curr_item_max_values.append(table[j-1][w])
            else:
                curr_item_max_values.append(max(
                    table[j-1][w],
                    values[j-1] + table[j-1][w-weights[j-1]])
                )
        table.append(curr_item_max_values)
    return table[-1][-1]


# more space efficient
def solve(values, weights, limit):
    table = [0 for _ in range(limit + 1)]
    for j in range(1, len(values) + 1):
        curr_item_max_values = [0]
        for w in range(1, limit + 1):
            if weights[j-1] > w:
                curr_item_max_values.append(table[w])
            else:
                curr_item_max_values.append(max(
                    table[w],
                    values[j-1] + table[w-weights[j-1]])
                )
        table = curr_item_max_values
    return table[-1]


v = [10, 40, 30, 50]
w = [5, 4, 6, 3]
l = 10
print(solve(v, w, l) == 90)


v = [20, 2, 4, 6, 7, 8, 10]
w = [1, 4, 4, 5, 4, 4, 7]
l = 10
print(solve(v, w, l) == 35)


v = [20, 2, 4, 6, 7, 8, 10]
w = [1, 4, 4, 5, 4, 4, 7]
l = 31
print(solve(v, w, l) == 57)


v = [10, 40, 30, 50]
w = [5, 4, 6, 3]
l = 100
print(solve(v, w, l) == 130)
