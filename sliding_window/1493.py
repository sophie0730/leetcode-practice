class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        k = 1
        maxLength = currLength =  0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            currLength = right - left
            maxLength = max(currLength, maxLength)
        
        return maxLength