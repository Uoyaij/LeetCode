'''
# @Time : 2022/8/4 18:40
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


# 统计每一个字符最后出现的位置
# 从头遍历字符，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = [0 for _ in range(26)]
        for i in range(len(s)):
            map[ord(s[i]) - ord('a')] = i  # 统计每个字符最后出现的位置
        res = []
        left, right = 0, 0
        for i in range(len(s)):
            right = max(right, map[ord(s[i]) - ord('a')])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res


S = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(S))
