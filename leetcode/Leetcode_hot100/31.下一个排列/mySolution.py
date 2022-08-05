'''
# @Time : 2022/7/20 18:29
# @Author : Admin
# @Project : PythonCode

返回恰好比nums排列后大的数，如果nums排列后是最大的，就返回最小的数


过程:
1, 5, (8), 7, 6, 2, 1 -> 1, (6), 8, 7, (5), 2, 1 -> 1, 6, 1, 2, 5, 7, 8
'''

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        j = len(nums) - 1
        while i > 0:
            if nums[i] <= nums[i - 1]:  # 从尾部找数
                i = i - 1
            else:
                break
        print('i:', i)
        if i > 0:
            while j > i - 1:    # 从i后面找一个比i-1大的数
                if nums[j] <= nums[i - 1]:
                    j = j - 1
                else:
                    break
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        # 翻转
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1

    def nextPermutation2(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


nums = [1, 5, 8, 7, 6, 2, 1]
nums1 = [8, 7, 6, 5, 4, 3, 2]
solution = Solution()
solution.nextPermutation(nums1)
print(nums1)
