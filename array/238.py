# if we would like to get the product of all the elements of nums except nums[i]
# we can use two arrays - prefix and suffix
# prefix is the product of all elements before nums[i]
# suffix is the product of all elements after nums[i]
# the product of prefix[i] and suffix[i] is the answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n # create an array of length n, filled '1' to each element
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]