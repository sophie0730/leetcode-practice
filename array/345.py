# use two pointer,start and end pointers.
# set a word which including all vowels, lowercase and uppercase.
# if both pointers are vowels, swap them.
# if start pointer is not a vowel, check the next elements
# if end pointer is not a vowel, check the former one.

class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        start = 0
        end = len(word) - 1
        vowels = 'aeiouAEIOU'

        while start < end:
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            while start < end and vowels.find(word[end]) == -1:
                end -= 1

            word[start], word[end] = word[end], word[start]

            #keep checking
            start += 1
            end -= 1
        
        return "".join(word)