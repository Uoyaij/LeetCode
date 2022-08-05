'''
# @Time : 2022/7/28 20:39
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:len(s)] + s[0:n]

    # 反转
    def reverseLeftWords1(self, s: str, n: int) -> str:
        s = list(s)
        s[0:n] = list(reversed(s[0:n]))  # 反转前n个
        s[n:] = list(reversed(s[n:]))  # 反转后n个
        s.reverse()  # 整个反转

        return "".join(s)

    # 遍历
    def reverseLeftWords2(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)

    # 不用.join
    def reverseLeftWords3(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res


s = "abcdefg"
k = 2
solution = Solution()
print(solution.reverseLeftWords(s, k))
