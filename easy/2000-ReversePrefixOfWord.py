class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                word = word[: i + 1][::-1] + word[i + 1 :]
                break
        return word


print(Solution().reversePrefix('abcdefd', 'd'))
