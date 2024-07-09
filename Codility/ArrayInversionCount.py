# 找出陣列中前面index比後面index值還大的排列組合有幾種
# time complexity: O(Nlog(N))


def mergesort_and_count(arr, temp_arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = 0

    inv_count += mergesort_and_count(
        arr, temp_arr, left, mid
    )  # divide left part to minimun element
    inv_count += mergesort_and_count(arr, temp_arr, mid + 1, right)  # divide right
    inv_count += merge_and_count(
        arr, temp_arr, left, mid, right
    )  # merge left and right, then count inversion

    return inv_count


def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left  # Starting index to be sorted
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]  # store sorted element
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += mid - i + 1
            if inv_count > 1000000000:
                return -1
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def solution(A):
    n = len(A)
    temp_arr = [0] * n
    inv_count = mergesort_and_count(A, temp_arr, 0, n - 1)
    if inv_count > 1000000000:
        return -1
    else:
        return inv_count


print(solution([-1, 6, 3, 4, 7, 4]))  # 輸出: 4


# Initial Array: [-1, 6, 3, 4, 7, 4]
# Step 1 : Split into two halves
# [-1, 6, 3]  [4,7,4]

# Step 2 : Continue splitting
# [-1] [6, 3]  [4]  [7,4]

# Step 3: Furhter splitting
# [-1]  [6] [3]    [4]  [7] [4]

# Step 4 : Merge and count inversions
# [-1]  [3,6]   [4]  [4,7]
#          (1)        (1)

# Step 5 : Merge larger halves and count inversions
# [-1, 3, 6]   [4, 4, 7]
#     (0)         (0)

# Step 6: Final merge and count inversions
# [-1, 3, 4, 4, 6, 7]
#       (2) [4,6][4,6]
