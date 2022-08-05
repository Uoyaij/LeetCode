'''
# @Time : 2022/7/25 21:30
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        nums = [[0 for _ in range(n)] for _ in range(n)]
        startx, starty = 0, 0  # 起始点
        loop, mid = n // 2, n // 2  # 迭代次数、n为奇数时，矩阵的中心点
        count = 1  # 计数

        for offset in range(1, loop + 1):  # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset):  # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):  # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1  # 更新起始点
            starty += 1

        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums

    def generateMatrix1(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range((n))]
        print(nums)
        startx, starty = 0, 0
        loop = n // 2
        count = 1
        for offset in range(1, loop + 1):
            for i in range(starty, n - offset):  # 从左到右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):  # 从上到下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右到左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下到上
                nums[i][startx] = count
                count += 1
            startx += 1
            starty += 1
        if n % 2 == 1:  # 奇数需要填充中心
            nums[loop][loop] = count
        return nums

    def generateMatrix2(self, n: int) -> List[List[int]]:
        left, right, up, down = 0, n - 1, 0, n - 1  # 定位四个方向的边界，闭区间
        res = [[0] * n for _ in range(n)]
        count = 1
        while True:
            for i in range(left, right + 1):  # 上边，从左到右
                res[up][i] = count
                count += 1
            up += 1  # 上边界下移
            if count > n * n:  # 判断是否已经遍历完
                break
            for i in range(up, down + 1):  # 右边，从上到下
                res[i][right] = count
                count += 1
            right -= 1  # 右边界左移
            if count > n * n:  # 判断是否已经遍历完
                break
            for i in range(right, left - 1, -1):  # 下边，从右到左
                res[down][i] = count
                count += 1
            down -= 1  # 下边界上移
            if count > n * n:  # 判断是否已经遍历完
                break
            for i in range(down, up - 1, -1):  # 左边，从下到上
                res[i][left] = count
                count += 1
            left += 1  # 左边界右移
            if count > n * n:  # 判断是否已经遍历完
                break
        return res


n = 4
solution = Solution()
print(solution.generateMatrix2(n))
