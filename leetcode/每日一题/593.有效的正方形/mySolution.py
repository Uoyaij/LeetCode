'''
# @Time : 2022/7/29 17:44
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        a = ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** (1 / 2)
        b = ((p3[1] - p1[1]) ** 2 + (p3[0] - p1[0]) ** 2) ** (1 / 2)
        c = ((p4[1] - p1[1]) ** 2 + (p4[0] - p1[0]) ** 2) ** (1 / 2)
        d = ((p3[1] - p2[1]) ** 2 + (p3[0] - p2[0]) ** 2) ** (1 / 2)
        e = ((p4[1] - p2[1]) ** 2 + (p4[0] - p2[0]) ** 2) ** (1 / 2)
        f = ((p4[1] - p3[1]) ** 2 + (p4[0] - p3[0]) ** 2) ** (1 / 2)
        set1 = set()
        set1.add(a)
        set1.add(b)
        set1.add(c)
        set1.add(d)
        set1.add(e)
        set1.add(f)
        if len(set1) > 2 or 0 in set1:
            return False
        else:
            return True

    def validSquare1(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        ans = set()
        temp = [(p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), (p3, p4)]
        for i in temp:
            distance = ((i[0][0] - i[1][0]) ** 2) + ((i[0][1] - i[1][1]) ** 2)
            ans.add(distance)
        return True if len(ans) == 2 and 0 not in ans else False


p1 = [0, 0]
p2 = [1, 1]
p3 = [0, 0]
p4 = [0, 0]
solution = Solution()
print(solution.validSquare(p1, p2, p3, p4))
