'''
# @Time : 2022/7/28 15:31
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            for j in range(i + 1, len(nums)):       # 这部分看作是三数之和即可
                if nums[j] == nums[j - 1] and j > i + 1:
                    continue
                left1 = j
                left2 = left1 + 1
                right = len(nums) - 1
                while left2 < right:
                    if nums[i] + nums[left1] + nums[left2] + nums[right] == target:
                        res.append([nums[i], nums[left1], nums[left2], nums[right]])  # 添加到res数组中
                        while left2 < right and nums[left2 + 1] == nums[left2] and nums[left2] == nums[left1]:  # 防止重复
                            left2 = left2 + 1
                        while left2 < right and nums[right] == nums[right - 1]: # 防止重复
                            right = right - 1
                        left2 = left2 + 1
                        right = right - 1
                    elif nums[i] + nums[left1] + nums[left2] + nums[right] > target:
                        right = right - 1
                    else:
                        left2 = left2 + 1
        return res


nums = [1, -2, -5, -4, -3, 3, 3, 5]
target = -11
solution = Solution()
print(solution.fourSum(nums, target))
