# use two pointer left and right
# sorting the array and iterate all elements by two pointers
# if the left element pluses the right element is equal to k, removing it, and increment operation
# the time complexity of sorting algorithm is O(nlogn), and the two pointer iteration is O(n). So, overall time complexity is O(nlogn)
# space complexity is O(1), since it uses the constant amount of spaces, regardless of the input size

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
       left, right = 0, len(nums) - 1
       operation = 0

       nums.sort()

       while left < right:
            if nums[left] + nums[right] == k:
               operation += 1
               left += 1
               right -= 1 # keep searching
            elif nums[left] + nums[right] < k:
               left += 1 # approaching k
            else:
               right -= 1

       return operation