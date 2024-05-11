from typing import List
from heapq import heappop, heappush


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])
        maxheap = []
        quality_sum = 0
        max_ratio = 0.0

        for i in range(k):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            # adding negative values creates a max heap
            # so it pops the highest value first
            heappush(maxheap, -ratio[i][1])

        res = max_ratio * quality_sum

        for i in range(k, len(wage)):
            max_ratio = max(max_ratio, ratio[i][0])
            # we would need to substract heappop(maxheap)
            # but since those are negative values, we just add them
            quality_sum += ratio[i][1] + heappop(maxheap)
            heappush(maxheap, -ratio[i][1])
            res = min(res, max_ratio * quality_sum)

        return res
