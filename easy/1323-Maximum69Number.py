"""
1323. Maximum 69 Number
https://leetcode.com/problems/maximum-69-number/
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        num_list = list(str(num))
        for i, x in enumerate(num_list):
            if x == "6":
                num_list[i] = "9"
                break
        return int("".join(num_list))


print(Solution.maximum69Number(Solution(), 9699))
