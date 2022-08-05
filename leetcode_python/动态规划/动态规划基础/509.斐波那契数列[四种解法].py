'''
# @Time : 2022/8/4 20:29
# @Author : Admin
# @Project : PythonCode
'''
from typing import List


class Solution:
    # dp
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        p = 0
        q = 0
        r = 1
        for i in range(2, n + 1):
            p = q
            q = r
            r = p + q
        return r

    # 递归
    def fib1(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        else:
            return self.fib1(n - 1) + self.fib1(n - 2)

    # 矩阵快速幂
    def fib3(self, n: int) -> int:
        if n < 2:
            return n

        q = [[1, 1], [1, 0]]
        res = self.matrix_pow(q, n - 1)
        return res[0][0]

    def matrix_pow(self, a: List[List[int]], n: int) -> List[List[int]]:
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ret = self.matrix_multiply(ret, a)
            n >>= 1
            a = self.matrix_multiply(a, a)
        return ret

    def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c

    # 通项公式
    def fib4(self, n: int) -> int:
        sqrt5 = 5 ** 0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)


n = 3
solution = Solution()
print(solution.fib1(n))
