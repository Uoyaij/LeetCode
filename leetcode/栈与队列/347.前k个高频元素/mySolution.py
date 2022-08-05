'''
# @Time : 2022/7/29 15:46
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    # 哈希表
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        res = []
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        dict1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)  # x[1]获取每个元素的第一个元素，reverse=True按降序排列
        for i in range(k):
            res.append(dict1[i][0])
        return res

    # 堆排序 #时间复杂度：O(nlogk) #空间复杂度：O(n)
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        import heapq
        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1    #get nums[i]没有就设置0，有就设置加1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))
