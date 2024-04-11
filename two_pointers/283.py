# use two pointer: left and right, both start at index 0
# if right pointer is not zero, swap left and right, since we should put zero to the right side
# after swaping, left index ++, 
# if not(right pointer is zero), the left pointer is no need to move, but move the right pointer to the next index.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums