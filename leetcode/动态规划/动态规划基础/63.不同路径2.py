'''
# @Time : 2022/8/5 10:03
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):  # 控制行
            for j in range(n):  # 控制列
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == j == 0:
                    continue
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


obstacleGrid = [[0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))
