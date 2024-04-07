# run a for loop, split the string to an array and reverse it.
# concat them using " "


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(s[::-1])