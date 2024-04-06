# First, we check str1 plus str2 if equals str2 plus str1
# if yes, we can find the common longest word
# and the length of the longest word is the greatest common divisor of the length of these two words
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]