'''
# @Time : 2022/7/22 20:48
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:

    # 暴力求解
    def maxSubArray(self, nums: List[int]) -> int:

        max = -10e5
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            flag = nums[i]
            if flag > max:
                max = flag
            for j in range(i + 1, len(nums)):
                flag = flag + nums[j]
                if flag > max and flag > nums[i]:
                    max = flag
        return max

    # 动态规划
    def maxSubArray1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre = 0
        maxAns = nums[0]
        for i in nums:
            pre = max(pre + i, i)
            maxAns = max(maxAns, pre)
        return maxAns

    # 贪心算法
    def maxSubArray3(self, nums: List[int]) -> int:
        result = -float('inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:  # 贪心策略，负数加下一个数，只会变小
                count = 0
        return result

    # 分治法
    def maxSubArray2(self, nums: List[int]) -> int:

        # 主函数
        left = 0
        # 左右边界
        right = len(nums) - 1
        # 求最大和
        maxSum = self.divide(nums, left, right)
        return maxSum

    def divide(self, nums, left, right):  # 如果只有一个元素就返回
        if left == right:
            return nums[left]
        # 确立中心点
        center = (left + right) // 2
        # 求子序在中心点左边的和
        leftMaxSum = self.divide(nums, left, center)
        # 求子序在中心点右边的和
        rightMaxSum = self.divide(nums, center + 1, right)

        # 求子序横跨2边的和，分成左边界和和右边界和
        leftBorderSum = nums[center]
        leftSum = nums[center]
        for i in range(center - 1, left - 1, -1):
            leftSum += nums[i]
            if leftSum > leftBorderSum:
                # 不断更新左区块的最大值
                leftBorderSum = leftSum
        rightBorderSum = nums[center + 1]
        rightSum = nums[center + 1]
        for i in range(center + 2, right + 1):
            rightSum += nums[i]
            if rightSum > rightBorderSum:
                # 不断更新右区块的最大值
                rightBorderSum = rightSum
        # 左边界的和 + 右边那块的和
        BorderSum = leftBorderSum + rightBorderSum
        return max(leftMaxSum, rightMaxSum, BorderSum)


nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray2(nums))
