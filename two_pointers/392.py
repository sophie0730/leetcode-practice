# traverse string t using pointer j
# if the current character of t matchs the current charater of s, increment i
# if i is equals to the length of s, means s is a substring of t


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
            
            j += 1

        return i == len(s)