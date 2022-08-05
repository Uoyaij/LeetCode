'''
# @Time : 2022/7/28 21:14
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1 = sorted(arr)
        num = 2  # 标号
        dict = {}
        res = []
        if not arr1:
            return []
        dict[arr1[0]] = 1
        for i in range(1, len(arr1)):
            if arr1[i] != arr1[i - 1]:
                dict[arr1[i]] = num
                num += 1
            else:
                dict[arr1[i]] = dict[arr1[i - 1]]
        for i in range(len(arr)):
            res.append(dict[arr[i]])
        return res

    def arrayRankTransform1(self, arr: List[int]) -> List[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]


arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
solution = Solution()
print(solution.arrayRankTransform1(arr))
