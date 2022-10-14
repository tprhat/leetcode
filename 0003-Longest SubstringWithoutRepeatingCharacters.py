"""
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(0, len(s)):
            curr_len = 1
            lst = [s[i]]
            for j in range(i + 1, len(s)):
                if s[j] in lst:
                    break
                lst.append(s[j])
                curr_len += 1
            if max_len < curr_len:
                max_len = curr_len
        return max_len
