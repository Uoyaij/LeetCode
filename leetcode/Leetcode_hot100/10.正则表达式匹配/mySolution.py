'''
# @Time : 2022/7/15 21:13
# @Author : Admin
# @Project : PythonCode

dp解法。
记dp[i][j]表示为s前i个字符和p前j个字符是否匹配
分情况讨论：
    1）当s[i] == p[j] 时， dp[i][j] = dp[i-1][j-1]
    2) 当p[j] == '.' 时， dp[i][j] = dp[i-1][j-1]
    3) 当p[j] == '*' 时
        3.1 if  s[i] != p[j-1]: dp[i][j] = dp[i][j-2] 因为，*可以把它前一位的给消掉。
        3.2 if  s[i] == p[j-1] or p[j-1] = '.'
            3.2.1 if '*'消除前面一位  dp[i][j] = dp[i][j-2]
            3.2.1 if '*'保留前面一位  dp[i][j] = dp[i][j-1]
            3.3.2 if '*'保留前面多位  dp[i][j] = dp[i-1][j], 说明第i位相同，观察前面一位即可。


'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # 初始化dp数组，因为需要考虑两边空串情况，所以行数和列数分别加1
        # 含空字串处理
        dp[0][0] = True  # 空字串为True
        for i in range(1, n + 1):       # dp行与列
            if p[i-1] == '*':           # dp第一行，空串遇见'*'，返回j-2状态
                dp[0][i] = dp[0][i-2]
            else:                       # 其余置false
                dp[0][i] = False
        for i in range(1, m + 1):       # 列置false
            dp[i][0] = False
        print(dp)
        for i in range(1, m + 1):       # 遍历，dp变化参照上述规则
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':  # 注意先判断相等的情况（细节）
                        dp[i][j] = (dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j])
                    else:
                        dp[i][j] = dp[i][j - 2]
        print(dp)
        return dp[m][n]




s = 'aab'
p = 'c*a*b'
solution = Solution()
print(solution.isMatch(s, p))
