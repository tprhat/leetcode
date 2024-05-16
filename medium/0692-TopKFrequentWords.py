"""
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
"""

from collections import Counter
from heapq import nsmallest
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lst = [(-cnt, word) for word, cnt in Counter(words).items()]
        return [word for _, word in nsmallest(k, lst)]
        # we use nsmallest with negative cnt values
        # so letter can alse be in a lexicographical ordel c < l


# print(Solution.topKFrequent(Solution(), words=["i", "love", "leetcode", "i", "love", "coding"], k=3))
