'''
# @Time : 2022/8/1 21:37
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True)  # 按绝对值大小排序
        print(nums)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k = k - 1
        if k > 0:
            nums[-1] = (-1) ** k * nums[-1]
        return sum(nums)


nums = [-2, 9, 9, 8, 4]
k = 5
solution = Solution()
print(solution.largestSumAfterKNegations(nums, k))
