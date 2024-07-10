# remove duplicate colors in a line
# leetcode 1578


def solutions(colors, needed_time):
    res = max_time = 0

    for i in range(len(colors)):
        if i > 0 and colors[i] != colors[i - 1]:
            max_time = 0

        res += min(max_time, needed_time[i])
        max_time = max(max_time, needed_time[i])

    return res


test_cases = solutions("abaac", [1, 2, 3, 4, 5])
test_cases1 = solutions("abc", [1, 2, 3])
test_cases2 = solutions("aabaa", [1, 2, 3, 4, 1])

print(test_cases)
print(test_cases1)
print(test_cases2)
