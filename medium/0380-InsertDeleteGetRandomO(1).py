"""
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""

import random


class RandomizedSet:
    def __init__(self):
        self.ids = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.ids:
            return False
        else:
            self.arr.append(val)
            self.ids[val] = len(self.arr) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.ids:
            return False

        self.ids[self.arr[-1]] = self.ids[val]
        self.arr[self.ids[val]] = self.arr[-1]
        self.ids.pop(val)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
