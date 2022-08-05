'''
# @Time : 2022/8/5 10:40
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] 表示拆分i获得的最大乘积
        dp = [0] * (n + 1)
        dp[2] = 1  # 初始化
        for i in range(3, n + 1):
            # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
            # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)       相当于拆分成两个数相乘
            # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]     相当于拆分成两个以上的数相乘
            for j in range(1, i - 1):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]

    def integerBreak1(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        res = 1
        while n > 4:  # 大于4的元素总是可以拆分成 2*(f-2)的 ，因为2*(f-2) > f
            res = res * 3
            n -= 3
        res = res * n
        return res


n = 10
solution = Solution()
print(solution.integerBreak1(n))
