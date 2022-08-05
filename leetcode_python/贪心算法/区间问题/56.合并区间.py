'''
# @Time : 2022/8/4 19:05
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) <= 1: return intervals
        intervals.sort(key=lambda x: x[0])  # 排序
        # print(intervals)
        start = intervals[0][0]  # 记录第一个start和end位置
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:  # 满足合并条件
                end = max(end, intervals[i][1])  # 合并
            else:  # 不满足合并条件
                res.append([start, end])  # 将先前的合并到新数组中
                start = intervals[i][0]  # 重新更新start,end
                end = intervals[i][1]
        res.append([start, end])  # 遍历结束，合并最后一个
        return res


intervals = [[1, 4], [0, 4]]
solution = Solution()
print(solution.merge(intervals))
