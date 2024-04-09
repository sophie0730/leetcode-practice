# the answer shold be the length of the decompressd word
# set a variable which counts the index

class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            
            # search same characters
            while i < len(chars) and chars[i] == letter: 
                count += 1
                i += 1 # keep searching, so in the next loop, we won't get the same element againt

            chars[ans] = letter # place the letter first in the array
            ans += 1
            
            # if the count greater than 10, we should split them by each digits
            for c in str(ans):
                chars[ans] = c
                ans += 1 # keep placing
        
        return ans