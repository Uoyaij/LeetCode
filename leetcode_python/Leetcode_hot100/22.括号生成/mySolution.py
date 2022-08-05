'''
# @Time : 2022/7/19 20:23
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:

    # DFS
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(str, left, right):
            """
            :param str: 当前字符串
            :param left: 左边剩余可用括号数
            :param right 右边剩余可用括号数
            :return:
            """
            if left == 0 and right == 0:
                res.append(str)
                return
            if left > right:  # 剪枝操作
                return
            if left > 0:
                dfs(str + '(', left - 1, right)
            if right > 0:
                dfs(str + ')', left, right - 1)

        str = ''
        res = []
        dfs(str, n, n)
        return res

    #  暴力破解
    def generateParenthesis2(self, n: int) -> List[str]:
        res = []

        def geneate(list: List):  # 列出所有情况
            if len(list) == 2*n:    # 长度到达2*n进行判断
                if isValid(list):
                    res.append("".join(list))
            else:
                list.append('(')
                geneate(list)
                list.pop()
                list.append(')')
                geneate(list)
                list.pop()

        def isValid(list: List):  # 判断是否满足括号条件
            ans = 0
            for i in range(len(list)):
                if list[i] == '(':
                    ans = ans + 1
                if list[i] == ')':
                    ans = ans - 1
                if ans < 0:
                    return False
            return ans == 0

        geneate([])
        return res


solution = Solution()

print(solution.generateParenthesis2(3))
