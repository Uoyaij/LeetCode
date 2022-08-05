'''
# @Time : 2022/7/26 21:03
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# 滑动窗口
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        nums = 2
        res = []
        count = 0
        maxCount = 0
        flag = 0
        for i in range(len(fruits)):
            if nums > 0 and fruits[i] not in res:
                res.append(fruits[i])
                nums = nums - 1
                count = count + 1
            elif fruits[i] in res:
                res.append(fruits[i])
                count = count + 1
            elif nums == 0:
                cal = len(res)
                for j in range(cal - 1, -1, -1):  # 开始滑动左指针
                    if res[j] != res[cal - 1]:
                        flag = j
                        break
                res = res[flag + 1:cal]
                res.append(fruits[i])  # 加入新水果
                count = count - (flag + 1) + 1  # 滑动剔除加水果计数+1
            maxCount = max(count, maxCount)
            print(res)
        return maxCount


fruits = [1, 2, 1, 1, 1, 3, 1, 1, 4]
solution = Solution()
print(solution.totalFruit(fruits))
