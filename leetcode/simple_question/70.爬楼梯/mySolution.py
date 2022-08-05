'''
# @Time : 2022/7/24 16:26
# @Author : Admin
# @Project : PythonCode
'''
from functools import lru_cache


class Solution:
    # 回溯法
    @lru_cache(None)  # 装饰器，防止内存移除
    def climbStairs(self, n: int) -> int:  # 超时
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # dp 迭代
    def climbStairs1(self, n: int) -> int:  # 超时
        # p, q, r = 0, 0, 1
        # for i in range(1, n+1):
        #     p = q
        #     q = r
        #     r = p+q
        # i = 0
        i = 0
        f2 = 0
        f1 = 0
        f = 1
        while i < n:
            f1 = f2
            f2 = f
            f = f1 + f2
            i = i + 1
        return f

    # 斐波那契数学公式


n = 38
solution = Solution()
print(solution.climbStairs1(n))
