'''
# @Time : 2022/7/31 10:39
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(startIndex, sum1):
            if sum1 == target:
                res.append(path[:])
                return
            if sum1 > target:
                return
            for i in range(startIndex, len(candidates)):
                if candidates[i] == candidates[i - 1] and i > startIndex:  # 去重
                    continue
                sum1 += candidates[i]
                    if target - candidates[i] < 0:
                        break
                path.append(candidates[i])
                backtrack(i + 1, sum1)
                sum1 -= candidates[i]  # 回溯
                path.pop()  # 回溯

        candidates.sort()  # sort排序方便剪枝
        print(candidates)
        backtrack(0, 0)
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
solution = Solution()
print(solution.combinationSum2(candidates, target))
