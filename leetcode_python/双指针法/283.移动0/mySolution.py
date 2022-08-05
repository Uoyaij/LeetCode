'''
# @Time : 2022/7/29 10:10
# @Author : Admin
# @Project : PythonCode
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = slow = 0
        while fast < len(nums):
            if nums[slow] != 0:
                slow += 1
            else:
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
            fast += 1
