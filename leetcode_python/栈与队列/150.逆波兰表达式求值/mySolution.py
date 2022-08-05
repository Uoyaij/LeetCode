'''
# @Time : 2022/7/29 14:01
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(i)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == "+":
                    stack.append(num1 + num2)
                if i == "-":
                    stack.append(num1 - num2)
                if i == "*":
                    stack.append(num1 * num2)
                if i == "/":
                    stack.append(num1 / num2)
        return int(stack[-1])


tokens = ["18"]
solution = Solution()
print(solution.evalRPN(tokens))
