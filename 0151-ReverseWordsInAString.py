"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(reversed(s.split())))
