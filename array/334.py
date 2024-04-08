# create two variables - first and second
# if num <= first, num maybe a potential first element
# if num > first and num <= second, num maybe a potential second element
# if  num > first and second, we got the third element, return true


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if first >= num:
                first = num
            elif second >= num:
                second = num
            elif second < num:
                return True
        return False