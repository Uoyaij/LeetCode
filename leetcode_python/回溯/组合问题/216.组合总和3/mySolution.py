'''
# @Time : 2022/7/30 21:08
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(k, n, startIndex):
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return
            for i in range(startIndex, 10-(k-len(path))+1):
                path.append(i)
                backtrack(k, n, i + 1)
                path.pop()

        res = []
        path = []
        backtrack(k, n, 1)
        return res


k = 3
n = 9
solution = Solution()
print(solution.combinationSum3(k, n))
