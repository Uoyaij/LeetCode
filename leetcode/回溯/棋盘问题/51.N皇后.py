'''
# @Time : 2022/8/1 10:44
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [['.' for _ in range(n)] for _ in range(n)]

        def isVaild(row, col, path):  # 不用判断行，因为递归就是向下递归的
            # if row == 1 and col == 0:
            #     print("进入")
            # 判断列
            for i in range(row):
                if path[i][col] == 'Q':
                    return False
            # 检查45°
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if path[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 检查135°
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if path[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # 都没有皇后
            return True

        def backtrack(row):
            # print(path)
            if row == n:
                temp_res = []
                for temp in path:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
                return
            for i in range(n):  # 代表列
                if isVaild(row, i, path):
                    path[row][i] = 'Q'
                    backtrack(row + 1)
                    path[row][i] = '.'  # 回溯
        backtrack(0)
        return res


n = 4
solution = Solution()
print(solution.solveNQueens(n))
