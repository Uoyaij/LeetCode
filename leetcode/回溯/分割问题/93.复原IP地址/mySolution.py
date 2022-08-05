'''
# @Time : 2022/7/31 14:19
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        res = []

        def vaild(temp):  # 合法性判断
            end = len(temp)
            if temp[0] == '0' and end != 1:
                return False
            return True

        def backtrack(startIndex=0):
            if startIndex >= len(s) and len(path) == 4:
                # res.append(path[:])
                res.append("".join(path[:]))
                return
            for i in range(startIndex, len(s)):
                temp = s[startIndex: i + 1]
                if 0 <= int(temp) <= 255 and vaild(temp):
                    if len(path) == 3:
                        path.append(temp)
                    else:
                        path.append(temp+'.')
                    backtrack(i + 1)
                    path.pop()
        backtrack()
        return res


s = "0000"
solution = Solution()
print(solution.restoreIpAddresses(s))
