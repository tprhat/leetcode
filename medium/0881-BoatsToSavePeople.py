from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            remaining = limit - people[left]
            boats += 1
            left += 1
            if left <= right and remaining >= people[right]:
                right -= 1

        return boats
