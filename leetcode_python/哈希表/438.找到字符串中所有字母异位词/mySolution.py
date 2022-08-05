'''
# @Time : 2022/7/27 20:43
# @Author : Admin
# @Project : PythonCode
'''
import collections
from typing import List


class Solution:
    # 暴力搜索
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        ans = []
        p_count = collections.Counter(p)  # 统计词频率
        for i in range(s_len - p_len + 1):  # 暴力搜索
            s_count = collections.Counter(s[i: i + p_len])
            if s_count == p_count:
                ans.append(i)
        return ans

    def findAnagrams1(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):  # 注意是p_len
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        print("s", s_count)
        print("p", p_count)
        if s_count == p_count:  # 首位一样
            ans.append(0)

        for i in range(s_len - p_len):
            print("s", s_count)
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans

    # 优化的滑动窗口
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res
        p_cnt = [0] * 26
        s_cnt = [0] * 26

        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1
        print(p_cnt)
        left = 0
        for right in range(n):  # 开始滑动
            cur_right = ord(s[right]) - ord('a')    # 存入s_cnt中
            s_cnt[cur_right] += 1
            while s_cnt[cur_right] > p_cnt[cur_right]:  # 字符不一致
                cur_left = ord(s[left]) - ord('a')  # 去除左边字符
                s_cnt[cur_left] -= 1
                left += 1   # 左边标记
            if right - left + 1 == m:   # 相等，存入left
                res.append(left)
        return res


s = "cbabeabacd"
p = "abc"

solution = Solution()
print(solution.findAnagrams2(s, p))
