'''
# @Time : 2022/8/4 9:53
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:

    # 身高按从大到小排序，次序按从小到大排序
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = sorted(people, key=lambda x: (-x[0], x[1]))
        for i in range(len(res)):
            temp = i - res[i][1]
            if temp > 0:
                for j in range(i, i - temp, -1):
                    res[j], res[j - 1] = res[j - 1], res[j]  # 交换
        return res


people = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
solution = Solution()
print(solution.reconstructQueue(people))
