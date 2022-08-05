'''
# @Time : 2022/7/23 20:57
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        length = len(s) - 1
        while length >= 0:
            if res > 0 and s[length] == ' ':
                return res
            if s[length] != ' ':
                res = res + 1
            length = length - 1
        return res


s = "luffy is still joyboy  a"
solution = Solution()
print(solution.lengthOfLastWord(s))
