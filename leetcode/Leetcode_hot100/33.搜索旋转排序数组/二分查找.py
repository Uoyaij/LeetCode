'''
# @Time : 2022/7/21 18:37
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# ---------二分-------------
# while left < right:
#     mid = (left + right) // 2
#     if nums[mid] < target:
#         left = mid + 1
#     elif nums[mid] > target:
#         right = mid - 1
#     else:
#         return mid


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:  # 说明左边有序
                if nums[0] <= target < nums[mid]:  # target在里面，然后二分求解
                    r = mid - 1
                else:
                    l = mid + 1  # 目标值不在，l=mid+1，跳到右边
            else:  # 说明右边有序
                if nums[mid] < target <= nums[len(nums) - 1]:  # target在里面，然后二分求解
                    l = mid + 1
                else:
                    r = mid - 1  # 目标值不在，r=mid-1，跳到左边
        return -1


nums = [1, 3, 4, 6, 8, 9, 13]
nums1 = [8, 9, 13, 1, 3, 4, 6]
nums2 = [4, 6, 8, 9, 13, 1, 3]
target = 6
solution = Solution()
print(solution.search(nums, target))
