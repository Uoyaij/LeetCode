'''
# @Time : 2022/7/31 15:22
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(startIndex=0):
            res.append(path[:])
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack()
        return res


nums = [1, 2, 3]
solution = Solution()
print(solution.subsets(nums))
