'''
# @Time : 2022/7/17 19:39
# @Author : Admin
# @Project : PythonCode


给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
'''

from typing import List


class Solution:
    # 暴力求解（超时）

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []

        def judge(array1: List[int], array2: List) -> bool:
            for i in range(len(array2)):
                b = sorted(array2[i])
                if sorted(array1) == b:
                    return False
            return True

        for i in range(len(nums)):  # 遍历
            x1 = 0 - nums[i]  # 找第一个元素
            for j in range(i + 1, len(nums)):
                x2 = x1 - nums[j]  # 找第二个元素
                if x2 in nums:
                    index = nums.index(x2)  # 找第三个元素
                    if index != i and index != j:  # 不是找到的之前的元素
                        temp = [nums[i], nums[j], nums[index]]  # 找到三元组
                        if judge(temp, res):
                            res.append(temp)
        return res

    # 双指针

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:  # nums长度不足3，返回空数组
            return []
        nums.sort()  # 排序
        print(nums)
        for i in range(len(nums)):  # 遍历
            if nums[i] > 0:  # 说明后面权大于0，无法构成三元组a+b+c=0，返回res
                return res
            if nums[i] == nums[i - 1] and i != 0:  # 防止重复
                continue
            left = i + 1  # 定义双指针
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])  # 添加到res数组中
                    while left < right and nums[left + 1] == nums[left]:  # 防止重复
                        left = left + 1
                    while left < right and nums[right - 1] == nums[right]:  # 防止重复
                        right = right - 1
                    left = left + 1  # 移动指针
                    right = right - 1
                elif nums[i] + nums[left] + nums[right] > 0:  # yu 结果>0，右指针向左移动
                    right = right - 1
                else:
                    left = left + 1  # 结果<0，左指针向右移动
        return res


nums = [0, 0, 0]
solution = Solution()
print(solution.threeSum2(nums))
