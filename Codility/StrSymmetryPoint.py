# Use two pointer
# time complexity: O(n)


def solution(S):
    if len(S) % 2 == 0:
        return -1

    mid = len(S) // 2
    left_str = S[0:mid]
    right_reverse = S[mid + 1 :][::-1]

    if left_str == right_reverse:
        return mid

    return -1
