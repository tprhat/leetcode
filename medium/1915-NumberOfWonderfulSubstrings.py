# https://leetcode.com/problems/number-of-wonderful-substrings/solutions/5090170/faster-lesser-3-methods-detailed-approach-prefix-xor-bitmask-frequency-python-java-c/
class Solution(object):
    def wonderfulSubstrings(self, word):
        count = [0] * 1024  # 2^10 to store bitmask frequencies
        count[0] = 1
        result = 0
        bitmask = 0

        for c in word:
            char_index = ord(c) - ord('a')
            bitmask ^= 1 << char_index
            result += count[bitmask]
            for i in range(10):
                result += count[bitmask ^ (1 << i)]
            count[bitmask] += 1

        return result
