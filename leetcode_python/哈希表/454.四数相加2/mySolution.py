'''
# @Time : 2022/7/28 15:08
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        首先定义 一个dict，key放a和b两数之和，value 放a和b两数之和出现的次数。
        """
        dict = {}
        for i in nums1:
            for j in nums2:
                if i + j in dict:
                    dict[i + j] += 1
                else:
                    dict[i + j] = 1
        print(dict)
        count = 0
        for i in nums3:
            for j in nums4:
                if -(i + j) in dict:
                    count += dict[-(i + j)]
        return count


nums1 = [-1, -1]
nums2 = [-1, 1]
nums3 = [-1, 1]
nums4 = [1, -1]
solution = Solution()
print(solution.fourSumCount(nums1, nums2, nums3, nums4))
