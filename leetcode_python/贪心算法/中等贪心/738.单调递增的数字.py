'''
# @Time : 2022/8/3 13:12
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        a = list(str(n))
        for i in range(len(a) - 1, 0, -1):      # 从后往前遍历
            if int(a[i]) < int(a[i - 1]):
                a[i - 1] = str(int(a[i - 1]) - 1)
                a[i:] = '9' * (len(a) - i)  # python不需要设置flag值，直接按长度给9就好了
        return int("".join(a))

n = 23222222
solution = Solution()
print(solution.monotoneIncreasingDigits(n))
