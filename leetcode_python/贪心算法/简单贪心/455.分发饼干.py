'''
# @Time : 2022/8/1 21:08
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                res = res + 1
                j = j + 1
            i = i + 1
        return res


g = [1, 2, 3]  # 胃口值
s = [1, 1]  # 尺寸

solution = Solution()
print(solution.findContentChildren(g, s))
