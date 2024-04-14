# bruce solution, time complexity: O(n^2)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        maxVowelCount = 0
        vowels = 'aeiouAEIOU'

        for i in range(k, len(s)+1):
            strSlice = s[start:i]
            currVowelCount = 0

            for element in strSlice:
                if element in vowels:
                    currVowelCount += 1

            maxVowelCount = max(maxVowelCount, currVowelCount)

            start += 1

        return maxVowelCount
    
# O(n) solution
# mainting the sliding window with size k, [i-k, i]
# coutn in/out the vowels during sliding
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = count = 0

        for i, c in enumerate(s):
            if (c in vowels):
                count += 1
            if i >= k and s[i - k] in vowels: # sliding the window, we should pop up the left element
                count -= 1

            ans = max(ans, count)

        return ans
                