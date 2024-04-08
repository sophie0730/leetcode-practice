# we should examine the elements before and after
# add a '0' to the first and last elements to handle edge cases

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1:i+2] == [0,0,0]:
                flowerbed[i] = 1
                n -= 1
        
        return n<=0