'''
# @Time : 2022/7/22 16:39
# @Author : Admin
# @Project : PythonCode



给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

你必须设计并实现时间复杂度为O(log n)的算法解决此问题。
'''

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIndex = self.binarySearch(nums, target, True)  # 寻找第一个大于等于target的索引
        rightIndex = self.binarySearch(nums, target, False) - 1  # 寻找第一个大于target的索引，然后-1是为了获得target末尾位置
        if leftIndex == len(nums):  # 说明没有找到
            return [-1, -1]
        if rightIndex < leftIndex:
            return [-1, -1]
        return [leftIndex,rightIndex]

    def binarySearch(self, nums, target, flag) -> int:
        l, r = 0, len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target or (flag and nums[mid] >= target):  # 方便代码复用
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans


class find:
    def findleftIndex(self, nums: List[int], target: int) -> int:  # 找第一个等于target的数
        l, r = 0, len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans

    def findrightIndex(self, nums: List[int], target: int) -> int:  # 找第一个大于target的数
        l, r = 0, len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans


# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]

# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
nums = [1, 2,3,3,3,3,5]
target = 1
solution = Solution()
print(solution.searchRange(nums, target))
# find = find()
# print(find.findleftIndex(nums, target))
# print(find.findrightIndex(nums, target))
