'''
# @Time : 2022/7/28 9:27
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        resSet = set()
        for i in nums1:
            if i in nums2:
                resSet.add(i)
        return list(resSet)

    # STL
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            num1 = nums1[index1]
            num2 = nums2[index2]
            if num1 == num2:
                # 保证加入元素的唯一性
                if not intersection or num1 != intersection[-1]:
                    intersection.append(num1)
                index1 += 1
                index2 += 1
            elif num1 < num2:
                index1 += 1
            else:
                index2 += 1
        return intersection

    # set比较
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)  # 不重复列表
        set2 = set(nums2)
        return self.set_intersection1(set1, set2)

    def set_intersection1(self, set1, set2):
        # if len(set1) > len(set2):  # 用短的遍历长的
        #     return self.set_intersection1(set2, set1)
        return [x for x in set1 if x in set2]


List1 = [1, 2, 3]
List2 = [1, 2, 2, 2]
solution = Solution()
print(solution.intersection(List1, List2))
