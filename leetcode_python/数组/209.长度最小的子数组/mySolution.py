'''
# @Time : 2022/7/25 16:48
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:

    # 暴力破解
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minRes = 10e6
        for i in range(len(nums)):
            flag = nums[i]
            if flag >= target:
                return 1
            count = 1
            for j in range(i + 1, len(nums)):
                flag = flag + nums[j]
                count = count + 1
                if flag >= target:
                    if count < minRes:
                        minRes = count
                        break
        if minRes == 10e6:
            return 0
        else:
            return minRes

    # 滑动窗口
    # 窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。
    # 窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        # 定义一个无限大的数
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= target:
                res = min(res, i - index + 1)  # 计算最小长度
                Sum -= nums[index]
                index += 1
        return 0 if res == float("inf") else res


target = 7
nums = [2, 3, 1, 2, 4, 3]
solution = Solution()
print(solution.minSubArrayLen1(target, nums))
