'''
# @Time : 2022/7/28 16:30
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


s = ["h", "e", "l", "l", "o"]
solution = Solution()
solution.reverseString(s)
print(s)
