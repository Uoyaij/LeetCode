'''
# @Time : 2022/7/26 10:40
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n - 1, 0, m - 1  # 定位四个方向的边界，闭区间
        res = []

        while True:
            for i in range(left, right + 1):  # 上边，从左到右
                res.append(matrix[up][i])
            up += 1  # 上边界下移
            if len(res) >= m * n:  # 判断是否已经遍历完
                break
            for i in range(up, down + 1):  # 右边，从上到下
                res.append(matrix[i][right])
            right -= 1  # 右边界左移
            if len(res) >= m * n:
                break
            for i in range(right, left - 1, -1):  # 下边，从右到左
                res.append(matrix[down][i])
            down -= 1  # 下边界上移
            if len(res) >= m * n:
                break
            for i in range(down, up - 1, -1):  # 左边，从下到上
                res.append(matrix[i][left])
            left += 1  # 左边界右移
            if len(res) >= m * n:
                break
        return res


matrix1 = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
matrix = [[1, 2, 3, 4]]

solution = Solution()
print(solution.spiralOrder(matrix1))
