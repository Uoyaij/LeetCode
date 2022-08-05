'''
# @Time : 2022/8/2 21:05
# @Author : Admin
# @Project : PythonCode
'''
from typing import List


class Solution:
    # 两次遍历
    def sortColors2(self, nums: List[int]) -> None:
        pre = 0
        for i in range(len(nums)):
            if nums[i] == 0:  # 交换零到前面
                nums[pre], nums[i] = nums[i], nums[pre]
                pre = pre + 1
        for i in range(pre, len(nums)):
            if nums[i] == 1:
                nums[pre], nums[i] = nums[i], nums[pre]
                pre = pre + 1

    # 一次遍历
    def sortColors3(self, nums: List[int]) -> None:
        p0, p1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 = p1 + 1
            elif nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:     # 说明1被换到后面去了，需要换回来
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 = p0 + 1
                p1 = p1 + 1

    # 计数排序
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        record = [0 for i in range(3)]
        for i in nums:
            record[i] += 1
        i, j = 0, 0
        while i < len(nums):
            if record[j] != 0:
                nums[i] = j
                record[j] -= 1
                i += 1
            else:
                j += 1

    # 快速排序
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1

        def quickSort(nums, left, right):
            if left < right:
                i, j = left, right
                temp = nums[left]
                while i < j:
                    while i < j and nums[j] >= temp:  # 从右往左找一个小于temp的数
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1
                    while i < j and nums[i] < temp:  # 从左往右找一个大于temp的数
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -= 1
                nums[i] = temp  # 完成一次快排
                quickSort(nums, left, i - 1)
                quickSort(nums, i + 1, right)

        quickSort(nums, left, right)


nums = [2, 1, 0]
solution = Solution()
solution.sortColors3(nums)
print(nums)
