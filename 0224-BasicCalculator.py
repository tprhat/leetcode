"""
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/
"""

class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, 1, [0]
        # sign = 1 if + and -1 if -
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            elif c == '+':
                stack[-1] += num * sign
                num = 0
                sign = 1
            elif c == '-':
                stack[-1] += num * sign
                num = 0
                sign = -1
            elif c == '(':
                stack.extend(([sign, 0]))  # add sign and 0 to sum inside brackets
                sign = 1
                num = 0
            elif c == ')':
                lastNum = (stack.pop() + num * sign) * stack.pop()  # 1.pop()=>sum inside, 2.pop()=>sign (+-1)
                stack[-1] += lastNum
                sign = 1
                num = 0

        return stack[-1] + num * sign

        # this works but it's very slow
        # result = 0
        # stack = []
        # helper = ''
        # s = s.strip()
        # # loading stack
        # for i, v in enumerate(s):
        #     if '0' <= v <= '9':
        #         helper += v
        #         if i == len(s) - 1:
        #             stack.append(helper)
        #     if v in '+-()':
        #         if helper:
        #             stack.append(helper)
        #         helper = ''
        #         stack.append(v)
        # if len(stack) == 1:
        #     return int(stack[0])
        # # adding brackets around the whole problem
        # stack.insert(0, '(')
        # stack.append(')')
        # while stack:
        #     if len(stack) == 1:
        #         result = int(stack.pop(0))
        #         break
        #     sign = stack.pop(0)
        #     stack1 = []
        #     # adding to stack1 everything inside brackets
        #     if sign == '(':
        #         stack1.append(sign)
        #         while sign != ')':
        #             sign = stack.pop(0)
        #             stack1.append(sign)
        #     else:
        #         stack.insert(0, sign)
        #     stack2 = []
        #     if stack1:
        #         stack1.pop() # remove the rightmost closing bracket
        #     # adding the inside bracket to evaluate
        #     if len(stack1) == 0:
        #         stack2 = stack
        #
        #     while stack1:
        #         sign = stack1.pop()
        #         if sign != '(':
        #             stack2.insert(0, sign)
        #         else:
        #             break
        #     # calculating
        #     while stack2:
        #         # if we have only '-' and a value left (3) then make it -value and add it to the stack
        #         if len(stack2) == 1:
        #             num = stack2.pop(0)
        #             stack.insert(0,num)
        #         elif len(stack2) == 2:
        #             num = stack2[0] + stack2[1]
        #             stack2.clear()
        #             stack.insert(0, num)
        #         else:
        #             # else do num1 +/- num2 and add it to stack
        #             if stack2[0] == '-':
        #                 stack2.pop(0)
        #                 num1 = '-' + stack2.pop(0)
        #             else:
        #                 num1 = stack2.pop(0)
        #             oper = stack2.pop(0)
        #             num2 = stack2.pop(0)
        #             if oper == '+':
        #                 val = str(int(num1) + int(num2))
        #             else:
        #                 val = str(int(num1) - int(num2))
        #             if len(stack2) == 0:
        #                 stack1.append(val)
        #             else:
        #                 stack2.insert(0, val)
        #     stack1.extend(stack)
        #     stack = stack1
        # return result
