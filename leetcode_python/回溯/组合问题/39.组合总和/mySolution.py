'''
# @Time : 2022/7/23 19:37
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# 对于这类寻找所有可行解的题，我们都可以尝试用「搜索回溯」的方法来解决。

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res,
                    target - candidates[index])  # 第二个参数为Index用来去重

        if not candidates:
            return []
        path = []  # 记录路径
        res = []
        size = len(candidates)
        dfs(candidates, 0, size, path, res, target)
        return res

    # 剪枝
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]  # 剪枝
                if residue < 0:
                    break
                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()       #注意这个sort,后面方便剪枝用
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(startindex=0):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(startindex, len(candidates)):
                startindex = i
                path.append(candidates[i])
                backtrack(startindex)
                path.pop()
        backtrack()
        return res


candidates = [2, 3, 6, 7]
target = 7
solution = Solution()
print(solution.combinationSum2(candidates, target))
