# 類似leetcode 529 簡單版


def solutions(n, r, c):
    ans = ""
    arr2d = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(r)):
        arr2d[r[i]][c[i]] = "B"

    for i in range(0, n):
        for j in range(0, n):
            bombnums = 0
            if arr2d[i][j] == "B":
                continue

            if i - 1 >= 0 and arr2d[i - 1][j] == "B":
                bombnums += 1
            if j - 1 >= 0 and arr2d[i][j - 1] == "B":
                bombnums += 1
            if i + 1 < n and arr2d[i + 1][j] == "B":
                bombnums += 1
            if j + 1 < n and arr2d[i][j + 1] == "B":
                bombnums += 1

            if i - 1 >= 0 and j - 1 >= 0 and arr2d[i - 1][j - 1] == "B":
                bombnums += 1
            if i - 1 >= 0 and j + 1 > n and arr2d[i - 1][j + 1] == "B":
                bombnums += 1
            if i + 1 > n and j - 1 >= 0 and arr2d[i + 1][j - 1] == "B":
                bombnums += 1
            if i + 1 > n and j + 1 >= 0 and arr2d[i + 1][j + 1] == "B":
                bombnums += 1

            arr2d[i][j] = bombnums

    for line in arr2d:
        ans += "".join(map(str, line)) + "\n"

    return ans


print(solutions(3, [2, 1, 0, 2], [0, 2, 1, 2]))
