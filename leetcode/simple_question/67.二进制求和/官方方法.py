'''
# @Time : 2022/7/24 10:50
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# 进制转换，先10后2
class Solution:
    def addBinary(self, a, b) -> str:
        print("aaa", 5 ^ 3)
        #        return '{0:b}'.format(int(a, 2) + int(b, 2))       # int(a,2) 为将a转换为10进制
        x = int(a, 2) + int(b, 2)
        print(x)
        return bin(x)[2:]

    # 位运算
    def addBinary1(self, a, b) -> str:      # x保存结果， y保存进位
        x, y = int(a, 2), int(b, 2)     # 转换为10进制
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    # 冒泡排序【与题目无关】
    def sort(self, num: List) -> List:
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]
        return num


a = '11'
b = '01'
nums = [2, 4, 1, 5, 7, 4, 2, 1]
solution = Solution()
print(solution.addBinary(a, b))
print(solution.sort(nums))
