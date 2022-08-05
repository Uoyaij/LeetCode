'''
# @Time : 2022/7/24 15:26
# @Author : Admin
# @Project : PythonCode
'''
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x + 1):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1

    # 袖珍计算器         思想 sqrt(x) = x^(1/2) = (e^(lnx))^(1/2) = e^((1/2)*lnx)
    def mySqrt1(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans  # 计算机无法存储浮点数的精确值，需要判断

    # 二分查找    思想k^2 <= x的最大k值
    def mySqrt2(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    # 牛顿法
    def mySqrt3(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


x = 2
solution = Solution()
print(solution.mySqrt2(int(x)))
