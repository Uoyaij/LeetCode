'''
# @Time : 2022/8/7 10:47
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # dp[i][j]：最多有i个0和j个1的strs的最大子集的大小为dp[i][j]。
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 默认初始化0
        # 遍历物品
        for str in strs:
            ones = str.count('1')
            zeros = str.count('0')
            # 遍历背包容量且从后向前遍历！
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)   # 选择装或不装
        return dp[m][n]


strs = ["10", "0001", "111001", "1", "0"]  # 物品
m = 4  # 二维背包
n = 3
solution = Solution()
print(solution.findMaxForm(strs, m, n))
