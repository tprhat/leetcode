import collections
from functools import cache
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        N = len(words)
        counts = collections.Counter(letters)

        @cache
        def get_score(index):
            f = collections.Counter(words[index])
            score_curr = 0
            for c, v in f.items():
                c = ord(c) - ord('a')
                score_curr += score[c] * v
            return score_curr
        
        def get_max(index, counts):
            if index == N:
                return 0
            
            best = 0

            # skip
            best = max(best, get_max(index + 1, counts))

            f = collections.Counter(words[index])
            if counts >= f:
                counts -= f
                score = get_score(index)
                best = max(best, get_max(index + 1, counts) + score)
                counts += f

            return best
        return get_max(0, counts)