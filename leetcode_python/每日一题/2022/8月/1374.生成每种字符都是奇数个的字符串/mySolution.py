'''
# @Time : 2022/8/1 9:34
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def generateTheString(self, n: int) -> str:
        res = ''
        i = 1
        while i <= n:
            if n % 2 == 1:  # 奇数
                if i == n-1:
                    res += 'b'
                elif i == n:
                    res += 'c'
                else:
                    res += 'a'
                i = i+1
            else:           # 偶数
                if i == n:
                    res += 'b'
                else:
                    res += 'a'
                i = i+1
        return res

    def generateTheString1(self, n: int) -> str:
        if n % 2 == 1:      # 奇数
            return "a" * n
        return "a" * (n - 1) + "b"  # 偶数

n = 15
solution = Solution()
print(solution.generateTheString(n))

