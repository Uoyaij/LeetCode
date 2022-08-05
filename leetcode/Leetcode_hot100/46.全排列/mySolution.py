'''
# @Time : 2022/7/24 19:02
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  # 表示从左往右填到第first个位置，当前排列为output

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])  # nums[:]表示创建一个完全相同的对象，否则前者的值会因为后者的值更改
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


nums = [1, 2, 3]
solution = Solution()
print(solution.permute(nums))
