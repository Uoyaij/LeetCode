'''
# @Time : 2022/7/15 19:21
# @Author : Admin
# @Project : PythonCode
'''


# 暴力搜索
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        maxnum = 0
        count = 0
        solution1 = Solution()
        length = len(s)
        for i in range(length):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    count = count + 1
                    if solution1.isPalindrome(s[i:j + 1]):
                        if len(s[i:j + 1]) > maxnum:
                            maxnum = len(s[i:j + 1])
                            left = i
                            right = j
        print(count)
        return s[left:right + 1]

    def isPalindrome(self, s: str) -> bool:  # 判断回文
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l = l + 1
                r = r - 1
            else:
                return False
        return True


# 优化暴力搜索[]
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        maxnum = 0
        solution1 = Solution()
        length = len(s)
        for i in range(length):
            for j in range(length - 1, i, -1):      # 从末尾开始
                if s[i] == s[j]:
                    if solution1.isPalindrome(s[i:j + 1]):  # 是回文串
                        if len(s[i:j+1]) > maxnum:
                            maxnum = len(s[i:j+1])
                            left = i
                            right = j
                        break
        return s[left:right+1]      # right+1可以处理单字符串回文

    def isPalindrome(self, s: str) -> bool:  # 判断回文
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l = l + 1
                r = r - 1
            else:
                return False
        return True




string = 'aacabdkacaa'
solution = Solution2()
print(solution.isPalindrome(string))
print(solution.longestPalindrome(string))
