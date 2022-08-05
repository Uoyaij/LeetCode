'''
# @Time : 2022/7/19 21:41
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        i = 0
        res = 0
        while i < len(s):
            if i + 1 < len(s) and dict[s[i]] < dict[s[i + 1]]:
                res = res + dict[s[i + 1]] - dict[s[i]]
                i = i + 2
            else:
                res = res + dict[s[i]]
                i = i + 1
        return res


s = 'VI'
solution = Solution()
print(solution.romanToInt(s))
