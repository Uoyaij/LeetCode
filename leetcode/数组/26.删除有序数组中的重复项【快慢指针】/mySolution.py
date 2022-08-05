'''
# @Time : 2022/7/21 20:13
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if i + 1 < length and nums[i] == nums[i + 1]:
                nums.pop(i)
                length = length - 1
            else:
                i = i + 1
        return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
print(solution.removeDuplicates(nums))
