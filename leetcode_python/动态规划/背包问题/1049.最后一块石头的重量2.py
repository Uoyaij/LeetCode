'''
# @Time : 2022/8/6 11:53
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 转换成01背包问题，求两堆石头的最小差值。由于石头总和为sum.则问题转换成了
        # 背包最多装sum / 2的石头, stones数组里有一大堆石头。求如何装能装下最多重量石头。
        target = sum(stones) // 2  # 背包容量
        dp = [0 for _ in range(target + 1)]  # dp[j] 表示背包容积为j能装下的最大价值
        for i in range(len(stones)):  # 物品
            for j in range(target, stones[i] - 1, -1):  # 背包体积
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return abs(dp[target] - (sum(stones) - dp[target]))


stones = [1]
stones1 = [31, 26, 33, 21, 40]
solution = Solution()
print(solution.lastStoneWeightII(stones))
