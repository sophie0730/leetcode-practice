# build a set for nums1, and find elements which are not in nums2
# build a set for num2, and find elements which are not in nums1

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = (n for n in set(nums1) if n not in nums2)
        second = (n for n in set(nums2) if n not in nums1)

        return first, second