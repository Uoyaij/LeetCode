'''
# @Time : 2022/7/29 13:53
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for i in s:
            if not stack:
                stack.append(i)
            elif i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)


s = "aaaa"
solution = Solution()
print(solution.removeDuplicates(s))
