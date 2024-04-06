# calculate the difference between the maximum of candies and extraCandies
# since the gauge plus extraCandies equals to the maximum of candies
# setting a "x" plus extraCandies, if it is greater than the gauge, it also greater than the maximum of candies



class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        gauge = max(candies) - extraCandies
        return [candy >= gauge for candy in candies]