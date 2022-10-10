class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negative = False
        number = ''
        for i, num in enumerate(s):
            if i == 0 and num in '-+':
                if num == '-':
                    negative = True
                continue

            if '0' <= num <= '9':
                number += num

            else:
                break
        if len(number) == 0:
            return 0
        number = int(number)
        if negative:
            number *= -1

        if number < -2 ** 31:
            return -2 ** 31
        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return number
