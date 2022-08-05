'''
# @Time : 2022/8/4 21:10
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # dp[i]表示到达i层所支付的最小费用
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        dp = [0 for _ in range(len(cost) + 1)]
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[len(cost)]

    # 滚动数组优化
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)
        prev = curr = 0  # 表示前一层和当前层
        for i in range(2, n + 1):
            nxt = min(curr + cost[i - 1], prev + cost[i - 2])  # 到第i层所需要的最小花费
            prev, curr = curr, nxt
        return curr


cost = [10, 15, 20]
cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
solution = Solution()
print(solution.minCostClimbingStairs(cost))
