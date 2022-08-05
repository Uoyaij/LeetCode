'''
# @Time : 2022/8/3 19:45
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:

    # 动态规划
    # 考虑到「不能同时参与多笔交易」，因此每天交易结束后只可能存在手里有一支股票或者没有股票的状态。
    # dp[i][0] 表示第i天交易后手里没有股票的最大利润
    # dp[i][1] 表示第i天交易后手里有股票的最大利润
    # dp[0][0] = 0
    # dp[0][1] = -price[0]
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[len(prices) - 1][0]

    def maxProfit1(self, prices: List[int], fee: int) -> int:
        res = 0
        buy = prices[0] + fee
        for i in range(1, len(prices)):
            if prices[i] + fee < buy:  # 可以选择买更小的股票
                buy = prices[i] + fee
            elif prices[i] > buy:     # 选择卖出股票
                res += prices[i] - buy
                buy = prices[i]     # 因为卖出的股票可能不是全局最优的，buy更新相当于我们手上有一个price[i]的股票，明天股票涨的话，就能获得price[i+1] - price[i]的利润
        return res


prices = [1, 3, 7, 5, 10, 3]
fee = 3
solution = Solution()
print(solution.maxProfit(prices, fee))
