'''
# @Time : 2022/7/23 21:28
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        flag = 0
        j = len(digits) - 1
        digits[j] = digits[j] + 1
        if digits[j] == 10:
            digits[j] = 0
            flag = 1
        j = j - 1
        while j >= 0:
            digits[j] = flag + digits[j]
            if digits[j] == 10:
                digits[j] = 0
                flag = 1
            else:
                flag = 0
            j = j - 1
        if flag > 0:
            digits.insert(0, 1)  # 或者digits = [1] + digits
        return digits

    def plusOne1(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        for j in range(len(digits) - 1, -1, -1):
            if digits[j] + 1 == 10:       # 判断尾部是否是9
                digits[j] = 0              # 置0，进位
            else:                       # 不是9，直接加1返回
                digits[j] = digits[j] + 1
                return digits
        digits = [1] + digits       # 都为9，首位添加1
        return digits


digits = [1, 2, 9]

solution = Solution()
print(solution.plusOne1(digits))
