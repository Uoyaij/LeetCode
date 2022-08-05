'''
# @Time : 2022/7/18 9:58
# @Author : Admin
# @Project : PythonCode

给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''

from typing import List


class Solution:

    # 列表推导式

    def letterCombinations(self, digits: str) -> List[str]:
        KEY = {'2': ['a', 'b', 'c'],  # 定义字典
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if digits == '':  # 空串
            return []
        ans = ['']  # 注意若ans = [], 无法进行字符相加。
        for num in digits:
            ans = [pre + suf for pre in ans for suf in KEY[num]]
            print("aaa", ans)
        return ans

    # 回溯法
    def letterCombinations2(self, digits: str) -> List[str]:
        res = []
        KEY = {'2': ['a', 'b', 'c'],  # 定义字典
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        def back(c, next):
            if len(next) == 0:
                res.append(c)
            else:
                for i in KEY[next[0]]:
                    back(c + i, next[1:])

        back('', digits)
        return res


digits = '234'
solution = Solution()
print(solution.letterCombinations2(digits))
