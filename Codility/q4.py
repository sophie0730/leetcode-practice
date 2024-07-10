# 找出二維陣列中相加起來最大的值
# 相加的兩個座標中，行座標和列座標都不能相等


def solutions(A):
    ans = 0
    flat_arr = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            element = {"value": A[i][j], "i": i, "j": j}
            flat_arr.append(element)

    flat_arr.sort(key=lambda x: x["value"], reverse=True)

    for i in range(len(flat_arr)):
        for j in range(1, len(flat_arr)):
            if (
                flat_arr[i]["i"] == flat_arr[j]["i"]
                or flat_arr[i]["j"] == flat_arr[j]["j"]
            ):
                continue

            tmp = flat_arr[i]["value"] + flat_arr[j]["value"]

            if ans < tmp:
                ans = tmp

    return ans


print(solutions([[12, 12], [12, 12], [0, 7]]))
print(solutions([[1, 2, 14], [8, 3, 15]]))
print(solutions([[1, 4], [2, 3]]))
