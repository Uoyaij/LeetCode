'''
# @Time : 2022/8/6 16:32
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # 原问题等同于： 找到nums一个正子集和一个负子集，使得总和等于target
    #
    # 我们假设P是正子集，N是负子集
    # 例如： 假设nums = [1, 2, 3, 4, 5]，target = 3，一个可能的解决方案是 + 1 - 2 + 3 - 4 + 5 = 3
    # 这里正子集P = [1, 3, 5]
    # 和负子集N = [2, 4]
    # 原问题转化： sum(p) = (sum(nums) + target) / 2  推导: P - N = target | P + N = sum(nums)

    # DP【二维数组】
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        sumValue = sum(nums)
        # 注意边界条件为 target>sumValue or target<-sumValue or  (sumValue + target) % 2 == 1
        if abs(target) > sumValue or (sumValue + target) % 2 == 1: return 0  # 若不加abs,定义数组时会出错
        bagSize = (sumValue + target) // 2
        dp = [[0 for i in range(bagSize + 1)] for j in range(len(nums) + 1)]  # dp[i][j]选取0-i物品填满容积j有dp[i][j]种方法
        # 初始化
        dp[0][0] = 1  # 一件物品都不选填满容积为1有一种方法
        for i in range(1, len(nums)+1):  # 遍历物品
            for j in range(bagSize + 1):  # 遍历背包容积
                if j < nums[i - 1]:  # 容量有限，无法选择第i个数字nums[i-1]
                    dp[i][j] = dp[i - 1][j]
                else:  # 可选择第i个数字nums[i-1]，也可不选【两种方式之和】
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
            print(dp)
        return dp[len(nums)][bagSize]

    # DP【一维数组】
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        sumValue = sum(nums)
        # 注意边界条件为 target>sumValue or target<-sumValue or  (sumValue + target) % 2 == 1
        if abs(target) > sumValue or (sumValue + target) % 2 == 1: return 0  # 若不加abs,定义数组时会出错
        bagSize = (sumValue + target) // 2
        print(bagSize)
        dp = [0] * (bagSize + 1)  # dp[j] 表示填满j容积背包有dp[j]种方法
        dp[0] = 1  # 填满0容积背包装0件物品，一种方法
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]  # 相当于把所有情况加起来，比如填了一个num[i]，相当于还有dp[j-num[i]]种方法，以此类推
            print(dp)
        return dp[bagSize]

    # 回溯法【超时】
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = []
        path = []
        if target > sum(nums): return 0
        if (sum(nums) + target) % 2: return 0  # 找不到这样的奇数子集，因为奇数除以2有小数
        needRes = (sum(nums) + target) // 2

        def backtrack(startIndex, sum):
            if sum == needRes:
                res.append(path[:])
                return
            for i in range(startIndex, len(nums)):
                if sum + nums[i] > needRes:
                    continue
                sum = sum + nums[i]
                path.append(nums[i])
                backtrack(i + 1, sum)
                sum = sum - nums[i]
                path.pop()

        nums.sort()  # 需要排序，不然漏解,比如 0,8. 如果先遍历8，就找不到{8,0}这个组合只有{8}这个组合
        backtrack(0, 0)
        return len(res)


nums = [1, 1, 1, 1, 1]
target = 3
solution = Solution()
print(solution.findTargetSumWays2(nums, target))
