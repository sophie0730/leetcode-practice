# sliding window problem
# first, initialize the maxSum and currSum to the first k elements of the array
# slide the window by a distance of 1 for the remaining elements of the array
# means, we should use the previous currSum, minus the left element and puls the right element
# if the currSum is greater than the maxSum, update the maxSum's value


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = nums[:k]

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]

            maxSum = max(maxSum, currSum)

        return maxSum / k