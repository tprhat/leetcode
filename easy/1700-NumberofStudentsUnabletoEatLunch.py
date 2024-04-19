from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones, zeros = students.count(1), students.count(0)
        for sandwich in sandwiches:
            if sandwich == 0 and zeros:
                zeros -= 1
            elif sandwich == 1 and ones:
                ones -= 1
            else:
                return ones + zeros

        return 0
