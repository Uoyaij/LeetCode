'''
# @Time : 2022/7/28 17:42
# @Author : Admin
# @Project : PythonCode
'''




class Solution:
    def replaceSpace(self, s: str) -> str:
        list1 = list(s)
        for i in range(len(list1)):
            if list1[i] == ' ':
                list1[i] = '%20'
        return ''.join(list1)
    # 双指针
    def replaceSpace1(self, s: str) -> str:
        counter = s.count(' ')

        res = list(s)
        # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        res.extend([' '] * counter * 2)
        print(res)
        # 原始字符串的末尾，拓展后的末尾
        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                # [right - 2, right), 左闭右开
                res[right - 2: right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)



s = "We are happy."
solution = Solution()
print(solution.replaceSpace1(s))

