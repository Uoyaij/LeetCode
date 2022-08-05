'''
# @Time : 2022/7/31 12:06
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def isPalindrome(str1):
            for i in range(len(str1) // 2):
                if str1[i] != str1[len(str1) - i - 1]:
                    return False
            return True

        def backtrack(startIndex):
            if startIndex >= len(s):    # 切割到最后
                res.append(path[:])
                return
            for i in range(startIndex, len(s)):
                temp = s[startIndex:i+1]   # 切割
                if isPalindrome(temp):     # 是回文串
                    path.append(temp)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return res


s = 'aaba'
solution = Solution()
print(solution.partition(s))
