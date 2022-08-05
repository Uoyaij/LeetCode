'''
# @Time : 2022/8/3 20:56
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# 你需要按照以下要求，给这些孩子分发糖果：

# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 如果是 87,87,2,1 意味着 分发糖果 1,3,2,1

# 采用左右贪心策略
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                res[j] = max(res[j], res[j + 1] + 1)  # 要比右边大
        return sum(res)

    # 环形糖果
    def candy1(self, ratings: List[int]) -> int:
        res = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        if ratings[0] > ratings[len(ratings) - 1]:
            res[0] = res[len(ratings) - 1] + 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                res[j] = max(res[j], res[j + 1] + 1)  # 要比右边大
        if ratings[len(ratings) - 1] > ratings[0]:
            res[len(ratings) - 1] = max(res[len(ratings) - 1], res[0] + 1)  # 要比右边大
        print(res)
        return sum(res)

ratings = [1, 2,3,4]
solution = Solution()
print(solution.candy1(ratings))
