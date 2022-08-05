'''
# @Time : 2022/8/4 21:22
# @Author : Admin
# @Project : PythonCode
'''
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):  # 控制行
            for j in range(n):  # 控制列
                if i == j == 0:
                    continue
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    # 空间优化
    def uniquePaths2(self, m, n):
        # 一维空间，其大小为 n
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # 等式右边的 dp[j]是上一次计算后的，加上左边的dp[j-1]即为当前结果
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]





    # 组合数学
    # 从左上角到右下角的过程中，我们需要移动 m+n-2 次，其中有 m-1次向下移动，n-1次向右移动。因此路径的总数，
    # 就等于从 m+n-2 次移动中选择 m-1 次向下移动的方案数，即组合数

    def uniquePaths1(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


m = 1
n = 12
solution = Solution()
print(solution.uniquePaths(m, n))
