'''
# @Time : 2022/8/2 9:42
# @Author : Admin
# @Project : PythonCode
'''

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

bills = [5,5,10,10,20]
solution = Solution()
print(solution.lemonadeChange(bills))
