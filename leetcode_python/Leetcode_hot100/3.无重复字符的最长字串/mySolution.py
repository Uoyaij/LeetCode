'''
# @Time : 2022/7/14 20:05
# @Author : Admin
# @Project : PythonCode
'''


# 暴力破解法

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        newStr = ""
        length = len(s)
        maxlength = 0
        for i in range(length):  # 遍历每位数字
            print("i:", i)
            for j in range(i, length):  # 从当前位置往后遍历
                if s[j] not in newStr:  # 不在就加入到新的newStr中
                    newStr = newStr + s[j]
                else:  # 存在一样的跳出该循环
                    print("跳出")
                    break
            length1 = len(newStr)  # 记录长度
            if length1 > maxlength:  # 记录最大长度
                maxlength = length1
            newStr = ""  # 清空newStr
        return maxlength


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        length = 0
        maxlen = 0
        for i in s:
            while i in temp:
                del temp[0]
                length = length - 1
            temp.append(i)
            print("temp:", temp)
            length = length + 1
            if length > maxlen:
                maxlen = length
        return maxlen


s = 'bacab'
solution = Solution2()
print(solution.lengthOfLongestSubstring(s))
