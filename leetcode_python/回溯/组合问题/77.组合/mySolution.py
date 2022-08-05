'''
# @Time : 2022/7/29 18:38
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # 存放符合条件结果的集合
        path = []  # 用来存放符合条件结果

        def backtrack(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, n + 1):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return res

    def combine1(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, n - (k - len(path)) + 2):  # 剪枝 已选择len(path)元素，还要k-len(path)元素，至多从n-(k-len(path))遍历
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return res


n = 4
k = 3
solution = Solution()
print(solution.combine(n, k))
