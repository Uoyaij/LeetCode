'''
# @Time : 2022/8/7 13:12
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# ！！！ 如果求组合数就是外层for循环遍历物品，内层for遍历背包。

# ！！！ 如果求排列数就是外层for遍历背包，内层for循环遍历物品。


class Solution:
    # 排列问题
    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)  # dp[j] 表示组成目标数有dp[j]种
        dp[0] = 1
        for i in range(1, target+1):    # 先遍历背包
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i -nums[j]]
        return dp[target]

    # 回溯【超时】
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        path = []

        def backtrack(sum):
            if sum == target:
                res.append(path[:])
                return
            for i in range(len(nums)):
                sum += nums[i]
                if sum > target:
                    continue
                path.append(nums[i])
                backtrack(sum)
                sum -= nums[i]
                path.pop()

        sum = 0
        nums.sort()
        backtrack(sum)
        return len(res)


# nums = [4, 2, 1]
nums = [1, 2, 3]
target = 4
solution = Solution()
print(solution.combinationSum4_1(nums, target))
