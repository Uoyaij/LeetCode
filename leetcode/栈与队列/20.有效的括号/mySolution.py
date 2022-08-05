'''
# @Time : 2022/7/18 20:10
# @Author : Admin
# @Project : PythonCode

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
'''


# 栈的思想

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:  # 奇串不可能正确
            return False
        Stack = []

        def Judge(s):  # 栈内判断
            if len(s) > 1:
                if s[len(s) - 1] + s[len(s) - 2] == 0 and s[len(s) - 2] < 0:  # 括号匹配判断，且需要左括号在前面
                    s.pop()
                    s.pop()

        for i in range(len(s)):  # 循环入栈
            if s[i] == '(':
                Stack.append(-1)
            elif s[i] == ')':
                Stack.append(1)
            elif s[i] == '[':
                Stack.append(-2)
            elif s[i] == ']':
                Stack.append(2)
            elif s[i] == '{':
                Stack.append(-3)
            elif s[i] == '}':
                Stack.append(3)
            Judge(Stack)
        if len(Stack) == 0:
            return True
        else:
            return False

    def isValid2(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        Stack = list()
        KEY = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        for i in s:  # 遍历字符串
            if i in KEY:  # 判断输入，如果是左括号直接入栈
                if not Stack:  # 右括号，且栈空，直接返回False
                    return False
                if Stack[-1] == KEY[i]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(i)
        return not Stack


string = '([}}])'
solution = Solution()
print(solution.isValid2(string))
