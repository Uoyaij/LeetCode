'''
# @Time : 2022/8/4 19:32
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum = 0
        for i in range(len(gas)):  # 计算净油量
            sum += gas[i] - cost[i]
        if sum < 0:  # 耗油大于加油,直接return
            return -1
        pre = 0  # 初始化
        index = 0  # 用于记录最大净油量的下标
        for i in range(len(gas)):
            if pre + gas[i] - cost[i] > gas[i] - cost[i]:  # 子序和和当前值比较
                pre = pre + gas[i] - cost[i]
            else:
                pre = gas[i] - cost[i]          # 当前值大，重新记录下标
                index = i
        return index


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

gas1 = [2, 3, 4]
cost1 = [3, 4, 3]
solution = Solution()
print(solution.canCompleteCircuit(gas1, cost1))
