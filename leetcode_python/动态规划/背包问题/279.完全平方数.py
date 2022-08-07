'''
# @Time : 2022/8/7 14:56
# @Author : Admin
# @Project : PythonCode
'''

# 这道题如果知道数学定理之后，相当于告诉你：
#
# 任何正整数都可以拆分成不超过4个数的平方和 ---> 答案只可能是1,2,3,4
# 如果一个数最少可以拆成4个数的平方和，则这个数还满足 n = (4^a)*(8b+7) ---> 因此可以先看这个数是否满足上述公式，如果不满足，答案就是1,2,3了
# 如果这个数本来就是某个数的平方，那么答案就是1，否则答案就只剩2,3了
# 如果答案是2，即n=a^2+b^2，那么我们可以枚举a，来验证，如果验证通过则答案是2
# 只能是3



class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)  # dp[i]表示满足i是完全平方数的最小数量
        dp[0] = 0
        for i in range(1, n + 1):  # 背包
            for j in range(1, n // 2 + 1):  # 物品
                if j * j > i:  # 这个剪枝比较重要，不然会浪费很多时间
                    break
                if i >= j * j:
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

    # 四平方和
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3


n = 8285
solution = Solution()
print(solution.numSquares(n))
