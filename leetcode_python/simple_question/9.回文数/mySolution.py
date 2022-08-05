'''
# @Time : 2022/7/19 21:25
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:  # 反转
        if x < 0:
            return False
        y = 0
        t = x
        while x:
            y = y * 10 + x % 10
            x //= 10
            return y == t


solution = Solution()
print(solution.isPalindrome2(827728))
