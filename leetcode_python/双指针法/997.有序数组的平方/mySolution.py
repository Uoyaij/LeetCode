'''
# @Time : 2022/7/25 16:35
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

    def sortedSquares1(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        i, j = 0, len(nums) - 1
        flag = len(nums) - 1
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                res[flag] = nums[i] * nums[i]
                i = i + 1
            else:
                res[flag] = nums[j] * nums[j]
                j = j - 1
            flag = flag - 1

        return res


nums = [0]
solution = Solution()
print(solution.sortedSquares1(nums))
