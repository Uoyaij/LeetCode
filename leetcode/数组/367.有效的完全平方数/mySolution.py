'''
# @Time : 2022/7/26 21:09
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    # 二分
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 0, num // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

    # 牛顿法
    class Solution:
        def isPerfectSquare(self, num: int) -> bool:
            x0 = num
            while True:
                x1 = (x0 + num / x0) / 2
                if x0 - x1 < 1e-6:
                    break
                x0 = x1
            x0 = int(x0)
            return x0 * x0 == num


num = 2
solution = Solution()
print(solution.isPerfectSquare(num))
