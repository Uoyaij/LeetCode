'''
# @Time : 2022/8/4 11:58
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0  # 跳跃次数
        cur = 0  # 记录当前覆盖最远距离
        next = 0  # 记录当前覆盖范围内的下一步可以覆盖的最远距离范围
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            next = max(nums[i] + i, next)
            if i == cur:
                if cur != len(nums) - 1:  # 未到终点
                    jump += 1
                    cur = next  # 更新当前覆盖距离
                    if next >= len(nums) - 1:
                        break
        return jump

nums = [2, 3, 1, 1, 4]
nums1 = [2, 2, 7, 1, 4]
solution = Solution()
print(solution.jump(nums))
