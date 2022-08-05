'''
# @Time : 2022/7/21 13:11
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        for i in range(len(strs[0])):   # 遍历数组第一个字符串的每一个字符
            for j in range(1, len(strs)):   # 观察数组其他字符串的每一个字符和他是否一样
                if i > len(strs[j]) - 1:    # 说明有数组长度受限制
                    return res
                if strs[0][i] != strs[j][i]:    # 有一个不一样，则返回
                    return res
            res = res + strs[0][i]
        return res


strs = [""]
solution = Solution()
print(solution.longestCommonPrefix(strs))
