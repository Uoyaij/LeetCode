'''
# @Time : 2022/8/1 9:58
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(startIndex):
            if startIndex == len(nums):
                res.append(nums[:])
            for i in range(startIndex, len(nums)):
                nums[i], nums[startIndex] = nums[startIndex], nums[i]
                backtrack(startIndex + 1)
                nums[startIndex], nums[i] = nums[i], nums[startIndex]

        backtrack(0)
        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(usage_list):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if usage_list[i]:
                    continue
                usage_list[i] = True
                path.append(nums[i])
                backtrack(usage_list)
                path.pop()
                usage_list[i] = False

        usage_list = [False] * len(nums)  # 记录纵向重复使用  491.记录横向重复使用
        backtrack(usage_list)
        return res


nums = [1, 2, 3]
solution = Solution()
print(solution.permute1(nums))
