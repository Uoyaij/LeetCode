'''
# @Time : 2022/7/16 9:10
# @Author : Admin
# @Project : PythonCode
'''


class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]  # 初始化
        for i in range(n):  # 自身一定回文
            dp[i][i] = True
        # 递推开始(动态规划按列递推)
        for j in range(1, n):  # 控制列
            for i in range(j):  # 控制行
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:  # 边界判断  因为 j-1 - (i+1) + 1 < 2时一i一定回文
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        print("dp", dp)
        return s[begin:begin + max_len]


string = 'adjdhjkd'
solution = Solution()
print(solution.longestPalindrome(string))
