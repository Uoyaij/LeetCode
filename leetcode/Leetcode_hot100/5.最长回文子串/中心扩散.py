'''
# @Time : 2022/7/16 9:11
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:  # 查找以该中心扩散回文的最大范围
            left -= 1
            right += 1
        return left + 1, right - 1          # 返回最大范围

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):                         # 遍历
            left1, right1 = self.expandAroundCenter(s, i, i)            # 中心是奇数 比如aba b是中心
            left2, right2 = self.expandAroundCenter(s, i, i + 1)        # 中心是偶数 比如abba bb是中心
            if right1 - left1 > end - start:        # 定位最大回文索引
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


string = 'abba'
solution = Solution()
print(solution.longestPalindrome(string))
