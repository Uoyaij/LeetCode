'''
# @Time : 2022/7/30 9:17
# @Author : Admin
# @Project : PythonCode
'''
import collections
import random
from typing import List


class Solution:
    # Hash表
    def majorityElement(self, nums: List[int]) -> int:
        list1 = {}
        # counts = collections.Counter(nums)
        # print(max(counts.keys(), key=counts.get))
        for i in nums:
            list1[i] = list1.get(i, 0) + 1
        print(list1)
        for i in list1:
            if list1[i] > len(nums) // 2:
                return i

    # 众数
    def majorityElement1(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # 随机化
    def majorityElement2(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

    # 摩尔投票法
    def majorityElement3(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        """
        核心就是对拼消耗。
        
        玩一个诸侯争霸的游戏，假设你方人口超过总人口一半以上，并且能保证每个人口出去干仗都能一对一同归于尽。最后还有人活下来的国家就是胜利。
        
        那就大混战呗，最差所有人都联合起来对付你（对应你每次选择作为计数器的数都是众数），或者其他国家也会相互攻击（会选择其他数作为计数器的数），但是只要你们不要内斗，最后肯定你赢。
        
        最后能剩下的必定是自己人。
        """
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
    # 分治法
    def majorityElement4(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)    # 左边的众数
            right = majority_element_rec(mid + 1, hi)  # 右边的众数

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner". 观察合并区间谁的数多
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)


nums = [2, 2, 1, 1, 1, 3, 2, 1, 1]
solution = Solution()
print(solution.majorityElement4(nums))
