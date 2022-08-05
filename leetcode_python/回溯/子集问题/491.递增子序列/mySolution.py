'''
# @Time : 2022/7/31 19:42
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(startIndex=0):
            if len(path) >= 2:
                res.append(path[:])
            # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
            usage_list = set()
            for i in range(startIndex, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in usage_list:
                    continue
                usage_list.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack()
        return res


nums = [1, 2, 3, 4, 1, 1, 1]
solution = Solution()
print(solution.findSubsequences(nums))
