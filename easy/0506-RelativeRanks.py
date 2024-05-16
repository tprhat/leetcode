from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        placments = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, x in enumerate(sorted(score, reverse=True)):
            if i < 3:
                score[score.index(x)] = placments[i]
            else:
                score[score.index(x)] = str(i + 1)

        return score
