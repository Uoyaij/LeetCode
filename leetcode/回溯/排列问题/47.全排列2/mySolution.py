'''
# @Time : 2022/8/1 10:31
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(use_list):
            if len(path) == len(nums):
                res.append(path[:])
                return
            record = set()      # 横向去重
            for i in range(len(nums)):
                if use_list[i] or nums[i] in record:
                    continue
                use_list[i] = True
                record.add(nums[i])
                path.append(nums[i])
                backtrack(use_list)
                path.pop()
                use_list[i] = False
        use_list = [False] * len(nums)  # 纵向去重
        backtrack(use_list)
        return res


nums = [1, 1, 2]
solution = Solution()
print(solution.permuteUnique(nums))
