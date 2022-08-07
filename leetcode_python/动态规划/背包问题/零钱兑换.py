'''
# @Time : 2022/8/7 14:39
# @Author : Admin
# @Project : PythonCode
'''
import functools
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  # dp[j] 表示凑成j需要的最少硬币数
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1  # 无解返回-1

    # 记忆化搜索
    def coinChange1(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1:
            return 0
        return dp(amount)


coins = [1, 2, 5]
amount = 11
solution = Solution()
print(solution.coinChange(coins, amount))
