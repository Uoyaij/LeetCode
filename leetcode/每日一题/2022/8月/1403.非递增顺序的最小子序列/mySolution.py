'''
# @Time : 2022/8/4 9:29
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        res = []
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)):
            res.append(nums[i])
            if sum(res) > sum(nums[i+1:len(nums)]):
                return res
        return res


nums = [6]
solution = Solution()
print(solution.minSubsequence(nums))
