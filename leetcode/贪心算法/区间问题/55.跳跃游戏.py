'''
# @Time : 2022/8/4 10:44
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # 贪心，覆盖范围
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1:
            return True
        i = 0
        while i <= cover:
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False


nums = [2, 3, 1, 1, 4]
solution = Solution()
print(solution.canJump(nums))
