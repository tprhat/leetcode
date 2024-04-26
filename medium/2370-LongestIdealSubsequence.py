class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # create a best array to store the best result for each character
        best = [0] * 26

        for c in s:
            curr = ord(c) - ord('a')

            start = max(0, curr - k)
            end = min(25, curr + k)

            best[curr] = best[curr] + 1

            # update the best result for each character
            for i in range(start, end + 1):
                if i != curr:
                    best[curr] = max(best[curr], best[i] + 1)

        return max(best)
