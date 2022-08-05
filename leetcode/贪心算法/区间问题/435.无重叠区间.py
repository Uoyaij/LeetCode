'''
# @Time : 2022/8/4 14:59
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        intervals.sort(key=lambda x: x[1])  # 右边界排序
        count = 1  # 记录非交叉区间的个数
        end = intervals[0][1]  # 记录区间分割点
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:  # 说明不交叉
                count += 1
                end = intervals[i][1]  # 更新分割点
        return len(intervals) - count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
solution = Solution()
print(solution.eraseOverlapIntervals(intervals))
