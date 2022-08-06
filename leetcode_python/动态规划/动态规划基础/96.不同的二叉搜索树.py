'''
# @Time : 2022/8/5 12:08
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):  # 2,  1*1 + 1*1  | 3 1*2 + 1*1 + 2*1
                dp[i] += dp[i - j] * dp[j - 1]

        return dp[n]


n = 3
solution = Solution()
print(solution.numTrees(n))
