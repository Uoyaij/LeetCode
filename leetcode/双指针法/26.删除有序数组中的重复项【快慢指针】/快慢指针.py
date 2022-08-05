'''
# @Time : 2022/7/21 20:45
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
print(solution.removeDuplicates(nums))
