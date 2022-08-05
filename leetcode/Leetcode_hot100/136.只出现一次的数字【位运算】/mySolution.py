'''
# @Time : 2022/7/30 9:00
# @Author : Admin
# @Project : PythonCode

  """
    交换律：a ^ b ^ c <=> a ^ c ^ b

    任何数于0异或为任何数 0 ^ n => n

    相同的数异或为0: n ^ n => 0
    """
'''
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a

    def singleNumber1(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums) # reduce 迭代器


nums = [2, 1, 3, 3, 1, 2, 4]
solution = Solution()
print(solution.singleNumber(nums))
