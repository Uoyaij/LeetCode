'''
# @Time : 2022/7/29 14:13
# @Author : Admin
# @Project : PythonCode
'''
import collections
from typing import List


class Solution:
    # 暴力搜索【超时】
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

    # 优化暴力【超时】
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        maxf = -float("inf")
        flag = 0
        res = []
        for i in range(k):
            if nums[i] >= maxf:
                maxf = nums[i]
                flag = i  # 记录最大值
        res.append(maxf)
        for i in range(1, len(nums) - k + 1):
            if i > flag:
                flag = nums.index(max(nums[i:i + k]))
                res.append(nums[flag])
            else:
                if nums[i + k - 1] >= nums[flag]:
                    flag = i + k - 1
                res.append(nums[flag])
        return res

    # 优先队列【nlogn】
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        import heapq
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]  # 创建索引数组
        heapq.heapify(q)  # 调整为小顶堆
        ans = [-q[0][0]]  # 获取堆顶元素【返回数组】
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))  # 入堆
            while q[0][1] <= i - k:  # 除掉左边元素【观察索引值是否在区间数组中】
                heapq.heappop(q)
            ans.append(-q[0][0])  # 添加调整后的堆顶元素

        return ans

    # 单调队列
    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):         # 维护窗口内的最大值
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        print(q)
        ans = [nums[q[0]]]      # 添加到返回数组中
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:     # 维护窗口最大值
                q.pop()
            q.append(i)
            while q[0] <= i - k:    # 不在窗口内
                q.popleft()
            ans.append(nums[q[0]])

        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow3(nums, k))
