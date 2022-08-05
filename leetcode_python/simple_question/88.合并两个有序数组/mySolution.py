'''
# @Time : 2022/7/25 10:35
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted  # 深复制

    # 逆向双指针 指针从后遍历，取两者之中的较大者放进nums1的后面，这种方法不会覆盖，
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


num1 = [1, 3, 4, 0, 0, 0, 0]
num2 = [1, 2, 3, 5]
solution = Solution()
solution.merge1(num1, 3, num2, 4)
print(num1)
