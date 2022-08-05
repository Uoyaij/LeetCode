'''
# @Time : 2022/8/4 13:09
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # 按照起始位置排序
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[0])  # 按起始位置排序
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:  # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界
        return result

    # 按照结束位置排序
    def finMinArrowShots2(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[1], reverse=True)
        result = 1
        for i in range(1, len(points)):
            if points[i][1] < points[i - 1][0]:  # 结束位置<起始位置
                result += 1
            else:
                points[i][0] = max(points[i][0], points[i - 1][0])
        return result


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
points1 = [[1, 2], [1, 4], [3, 5], [3, 6], [5, 7]]
solution = Solution()
print(solution.finMinArrowShots2(points1))
