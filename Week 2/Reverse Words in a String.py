# Given an input string, reverse the string word by word.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed([x for x in s.strip().split(" ") if x!=""]))
        
