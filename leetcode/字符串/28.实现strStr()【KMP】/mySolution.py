'''
# @Time : 2022/7/22 10:40
# @Author : Admin
# @Project : PythonCode


实现strStr()函数。

给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

说明：

当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(haystack)
        i = 0
        while i < length:       # 遍历haystack
            j = 0
            if haystack[i + j] == needle[j]:    # 找到第一个字符相等
                while j < len(needle):
                    if i + j >= length:         # haystack越界
                        return -1
                    if haystack[i+j] == needle[j]:  # 逐个字符比较
                        j = j + 1
                    else:                   # 匹配失败
                        break
                if j == len(needle):        #匹配成功
                    return i
            i = i + 1
        return -1


haystack = 'abacdbaksd'
needle = ''
solution = Solution()
print(solution.strStr(haystack, needle))
