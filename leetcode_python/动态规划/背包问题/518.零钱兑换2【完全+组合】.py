'''
# @Time : 2022/8/7 12:27
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # dp[j]表示金额为j时有dp[j]种换法
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):  # 物品
            for j in range(coins[i], amount + 1):  # 背包体积
                dp[j] += dp[j - coins[i]]       # 相当于不用新的coin换的时候的换法+用新的coin换的时候的换发
            print(dp)
        return dp[amount]


amount = 5
coins = [2, 2, 1]
solution = Solution()
print(solution.change(amount, coins))
