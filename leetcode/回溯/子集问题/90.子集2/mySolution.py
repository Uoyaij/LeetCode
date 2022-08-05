'''
# @Time : 2022/7/31 19:17
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(startIndex=0):
            res.append(path[:])
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:  # 去重
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack()
        return res


nums = [4, 1, 4, 4, 4]
nums.sort()  # 排序方便去重
solution = Solution()
print(solution.subsetsWithDup(nums))
