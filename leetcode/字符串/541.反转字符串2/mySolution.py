'''
# @Time : 2022/7/28 16:36
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        length = len(s)
        res = ''
        while i < length:
            if i % (2 * k) == 0:  # 反转前k个
                if length - i < k:  # 剩余字符不足k个，全部反转
                    res = res + s[i:length][::-1]
                    i = length
                else:
                    res = res + s[i:i + k][::-1]
                    i = i + k
            else:
                res = res + s[i]
                i = i + 1
        return res

    # 模拟
    def reverseStr1(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)


s = "a"
k = 2
solution = Solution()
print(solution.reverseStr1(s, k))
