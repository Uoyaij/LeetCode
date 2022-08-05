'''
# @Time : 2022/7/22 9:20
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums.pop(i)
                length = length - 1
            else:
                i = i + 1
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        left = right = 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left = left + 1
            right = right + 1
        return left

    def removeElement3(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right = right - 1
            else:
                left = left + 1
        return left


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
solution = Solution()
print(solution.removeElement2(nums, val))
print(nums)
