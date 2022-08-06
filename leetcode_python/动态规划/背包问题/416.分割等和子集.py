'''
# @Time : 2022/8/6 8:24
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # DP
    # 背包体积：sum / 2
    # 背包要放入的商品（集合里的元素）重量为 元素的数值，价值也为元素的数值
    # 背包如果正好装满，说明找到了总和为 sum / 2 的子集。
    # 背包中每一个元素是不可重复放入。
    def canPartition1(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False
        target = sum(nums) // 2  # 背包体积
        dp = [0 for j in range(target + 1)]  # 表示容量为j时，所装的物品的最大价值
        for i in range(len(nums)):  # 物品
            for j in range(target, nums[i] - 1, -1):  # 背包
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return target == dp[target]

    def canPartition2(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2  # 背包体积
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums))]  # dp[i][j]表示抽取0-i个物品放入体积j的背包中获得的最大价值
        # 初始化第一列
        for i in range(len(nums)):
            dp[i][0] = 0
        # 初始化第一行
        firstweight, firstValue = nums[0], nums[0]
        for i in range(1, target + 1):
            if firstweight <= i:
                dp[0][i] = firstValue
        # 状态转移
        for i in range(1, len(nums)):
            curweight, curValue = nums[i], nums[i]
            for j in range(1, target + 1):
                if curweight > j:  # 重量大，无法放入
                    dp[i][j] = dp[i - 1][j]
                else:  # 可以放入
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
        return target == dp[len(nums) - 1][target]

    # 回溯法【超时】
    def canPartition(self, nums: List[int]) -> bool:
        path = []

        def backtrack(startIndex, path):
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                if sum(path) == sum(nums) / 2:
                    return True
                backtrack(i + 1, path)
                path.pop()

        if backtrack(0, path):
            return True
        return False


nums = [1, 5, 11, 5, 1]
solution = Solution()
print(solution.canPartition2(nums))
