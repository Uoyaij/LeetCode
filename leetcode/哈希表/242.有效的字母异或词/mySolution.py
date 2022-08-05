'''
# @Time : 2022/7/27 20:11
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for j in t:
            if j not in dict:
                return False
            dict[j] -= 1
            if dict[j] < 0:
                return False
        return True

    def isAnagram1(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(s[i]) - ord("a")] += 1
        for i in range(len(t)):
            record[ord(t[i]) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                # record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
                # 如果有一个元素不为零，则可以判断字符串s和t不是字母异位词
        return True


s = "anagram"
t = "nagarmh"
solution = Solution()
print(solution.isAnagram1(s, t))
