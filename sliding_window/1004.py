# Initialize two pointers, left and right, both set to 0
# Employ a slidig window approach to traverse through the array. 
# If the current end element of the subarray is 0, flip it to 1 until k<0

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1