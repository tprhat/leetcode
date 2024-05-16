from typing import List, Any
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> deque[Any]:
        q = deque()
        for card in reversed(sorted(deck)):
            q.rotate()
            q.appendleft(card)
        return q
