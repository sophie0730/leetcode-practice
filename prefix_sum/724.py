# initialize leftsum and rightsum, to store all elements of the list
# iterate the list, if leftsum is not equal to rightsum, add the element to leftsum and minus this to right sum
# if leftsum is equal to right sum, return the index of this element

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)

        for index, element in enumerate(nums):
            rightSum -= element

            if rightSum == leftSum:
                return index
            
            leftSum += element

        return -1