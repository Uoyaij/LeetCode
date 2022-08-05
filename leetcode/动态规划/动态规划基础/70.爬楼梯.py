'''
# @Time : 2022/8/4 21:04
# @Author : Admin
# @Project : PythonCode
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for i in range(1, n+1):
            p = q
            q = r
            r = p+q
        return r