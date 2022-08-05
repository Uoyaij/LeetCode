'''
# @Time : 2022/7/14 21:35
# @Author : Admin
# @Project : PythonCode


解题思路：设置两个指针左右指针（left和遍历指针）
通过观察，我们依次枚举字串的起始位置，那么字串的结束位置也是递增的！！！
我们开始枚举下一个字符作为起始位置，然后我们可以不断地向右移动右指针，但需要保证这两个指针对应的子串中没有重复的字符。
以'abacda'为例子
开始遍历，首先ab进入到set中，(此时len=2)继续遍历到a时，发现重复,删除第一个a，即留下ba
继续添加cd，bacd进入到set中(此时len=4)，遍历到a时，发现重复，删除ba留下cda(此时len=3)，最后输出最大长度len=4
'''


# 滑动窗口

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0  # if not 判空用法 等价于 if s == ""
        left = 0
        lookup = set()  # set()创建一个无序不重复的元素集
        n = len(s)  # 计算长度
        max_len = 0  # 最大长度
        cur_len = 0  # 当前长度
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:  # 用于定位s[i]在lookup中的位置
                lookup.remove(s[left])  #
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
            print(lookup)
        return max_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0  # 最大长度
        tp = []  # 放字符串的一个队列
        for a in s:
            while a in tp:
                del tp[0]  # 删除队列左边第一个，直到没有重复的字符串
            tp.append(a)
            if len(tp) > max_len:
                max_len = len(tp)
        return max_len


s = 'abcad'
solution = Solution2()
print(solution.lengthOfLongestSubstring(s))
