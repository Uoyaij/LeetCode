'''
# @Time : 2022/7/22 20:36
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:  # 查找第一个大于等于 target的值
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res

    def searchInsert1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:  # 查找第一个大于等于 target的值
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return -1



nums = [1, 2, 5, 6]
target = 6
solution = Solution()
print(solution.searchInsert1(nums, target))
