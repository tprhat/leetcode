"""
Check if the Sentence Is Pangram
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)
        if len(s) == 26:
            return True
        return False
