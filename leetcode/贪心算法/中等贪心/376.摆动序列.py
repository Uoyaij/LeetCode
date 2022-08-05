'''
# @Time : 2022/8/3 10:36
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# 贪心

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        preC, curC, res = 0, 0, 1  # res 记录结果， preC, curC分别记录之前后差值（＋/-）
        for i in range(1, len(nums)):
            curC = nums[i] - nums[i - 1]
            if curC * preC <= 0 and curC != 0:  # 差值改变（说明摆动）
                res += 1
                preC = curC  # 记录差值
        return res

    # 动态规划
    # 容易发现当前考虑的这个数，要么作为山峰，要么作为山谷
    # dp[i][0] 前i个数，第i个数作为山峰摆动子序列的最长长度
    # dp[i][1] 前i个数，第i个数作为山谷摆动子序列的最长长度
    # 转移方程：dp[i][0] = max(dp[i][0], dp[j][1] + 1) 其中0<j<1 and num[j] < num[i]
    # 转移方程：dp[i][1] = max(dp[i][1], dp[j][0] + 1) 其中0<j<1 and num[j] > num[i]
    # 初始状态 dp[0][0] = dp[0][1] = 1
    def wiggleMaxLength2(self, nums: List[int]) -> int:

        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][1] = dp[0][0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        return max(dp[len(nums) - 1][1], dp[len(nums) - 1][0])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

solution = Solution()
print(solution.wiggleMaxLength2(nums))
