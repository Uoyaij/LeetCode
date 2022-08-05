'''
# @Time : 2022/7/15 13:24
# @Author : Admin
# @Project : PythonCode
'''


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        flag1 = 0
        flag2 = 0
        if len(nums1) == 0:  # nums1为空，返回nums2的中位数
            if len(nums2) % 2 == 0:  # 偶数
                return (nums2[int((len(nums2)) / 2)] + nums2[int((len(nums2)) / 2 - 1)]) / 2
            else:
                return nums2[int(len(nums2) / 2)]
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:  # 偶数
                return (nums1[int((len(nums1)) / 2)] + nums1[int((len(nums1)) / 2 - 1)]) / 2
            else:
                return nums1[int(len(nums1) / 2)]
        for i in range(len(nums1) + len(nums2)):  # 依次比较
            if nums1[flag1] < nums2[flag2]:
                nums3.append(nums1[flag1])
                flag1 = flag1 + 1
            else:
                nums3.append(nums2[flag2])
                flag2 = flag2 + 1
            if flag1 == len(nums1):  # nums1遍历结束，将nums2中的元素直接添加到nums3中
                nums3.extend(nums2[flag2:])
                break
            elif flag2 == len(nums2):
                nums3.extend(nums1[flag1:])
                break
        if len(nums3) % 2 == 0:  # 偶数
            return (nums3[int((len(nums3)) / 2)] + nums3[int((len(nums3)) / 2 - 1)]) / 2
        else:
            return nums3[int(len(nums3) / 2)]

    # 暴力破解简写
    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums, m, n = sorted(nums1 + nums2), len(nums1), len(nums2)  # sort直接排序
        return (nums[(m + n - 1) // 2] + nums[(m + n) // 2]) / 2  # //表示地板除，先除后向下取整，当有//左右两边有一个是float型，结果是float型

    # 最小K值法
    def findMedianSortedArrays3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findMinK(k: int) -> float:
            # 非正常情况
            index1, index2 = 0, 0  # 用于重新定位，因为一旦某个数组一些元素被排除，index就需要定位过去
            while True:
                # 特殊情况
                if len(nums1) == index1:  # nums1全部被去除，直接返回nums2中相对第k小值
                    return nums2[index2 + k - 1]
                if len(nums2) == index2:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, len(nums1) - 1)  # 从调整位置重新比较,且min函数防止越界，比如nums1=[1],nums2=[2,3,4,5,6]
                newIndex2 = min(index2 + k // 2 - 1, len(nums2) - 1)
                if nums1[newIndex1] <= nums2[newIndex2]:
                    k = k - (newIndex1 - index1 + 1)  # newIndex1 - index1 + 1 查看多少个数被排除，比如最小k值是4，排除2个小于k值的数，那么k调整为k=k-2
                    index1 = newIndex1 + 1
                else:
                    k = k - (newIndex2 - index2 + 1)
                    index2 = newIndex2 + 1

        length = len(nums1) + len(nums2)
        if length % 2 == 1:  # 奇数
            return findMinK((length + 1) // 2)
        else:
            print("a:", findMinK(length // 2))
            print("b:", findMinK(length // 2 + 1))
            return (findMinK(length // 2) + findMinK(length // 2 + 1)) / 2


nums1 = [2]
nums2 = [1, 3, 4]
solution = Solution()
print(solution.findMedianSortedArrays3(nums1, nums2))
