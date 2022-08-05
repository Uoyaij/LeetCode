'''
# @Time : 2022/8/3 19:00
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# 任何时候，你最多只能持有一股股票

# 以 1，5，6为例子， 看似结果为1购入，6售出
# 实际可以是 1 购入 5 售出  5 购入  6 售出
# 也就意味着只要今天比昨天大就卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res

    # 动态规划
    # 考虑到「不能同时参与多笔交易」，因此每天交易结束后只可能存在手里有一支股票或者没有股票的状态。
    # dp[i][0] 表示第i天交易后手里没有股票的最大利润
    # dp[i][1] 表示第i天交易后手里有股票的最大利润
    # dp[0][0] = 0
    # dp[0][1] = -price[0]
    def maxProfit1(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[len(prices) - 1][0]


prices = [1,3,2,8]
solution = Solution()
print(solution.maxProfit(prices))
