"""
Zigzag Conversion
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        listRows = [""] * numRows
        direction = -1
        lvl = 0
        for letter in s:
            listRows[lvl] += letter
            lvl -= direction
            if lvl == numRows - 1 or lvl == 0:
                direction *= -1

        return ''.join(listRows)
