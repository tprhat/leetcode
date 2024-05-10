from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fraction = (arr[i] / arr[j], (arr[i], arr[j]))
                heappush(minHeap, fraction)

        for i in range(k - 1):
            heappop(minHeap)

        return heappop(minHeap)[1]
