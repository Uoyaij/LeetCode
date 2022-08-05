'''
# @Time : 2022/7/28 9:58
# @Author : Admin
# @Project : PythonCode
'''
import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        print(nums1, nums2)
        res = []
        index1, index2 = 0, 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] > nums2[index2]:
                index2 = index2 + 1
            else:
                index1 = index1 + 1
        return res

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = collections.Counter(nums1)
        res = []
        for i in nums2:
            if i in dict and dict1[i] > 0:
                dict1[i] -= 1
                res.append(i)
        return res

List1 = [6, 4, 10, 2, 1, 2, 3]
List2 = [1, 2, 4, 2, 6, 7]
solution = Solution()
print(solution.intersect1(List1, List2))
