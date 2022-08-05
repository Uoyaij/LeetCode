'''
# @Time : 2022/7/24 9:53
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a: return b
        if not b: return a
        i = len(a) - 1
        j = len(b) - 1
        flag = 0  # 进位标志
        s = ''
        while i >= 0 and j >= 0:        # i和j存在时开始相加
            print(i, j)
            if (int(a[i]) + int(b[j]) + flag) >= 2:     # 需要进位
                s = s + str(int(a[i]) + int(b[j]) + flag - 2)
                flag = 1
            else:
                s = s + str(int(a[i]) + int(b[j]) + flag)
                flag = 0
            i = i - 1
            j = j - 1
        for x in range(j, -1, -1):      # 可能a遍历结束，继续遍历b
            if (int(b[x]) + flag) >= 2:
                s = s + str(int(b[x]) + flag - 2)
                flag = 1
            else:
                s = s + str(int(b[x]) + flag)
                flag = 0
        for x in range(i, -1, -1):  # 可能b遍历结束，继续遍历q
            if (int(a[x]) + flag) >= 2:
                s = s + str(int(a[x]) + flag - 2)
                flag = 1
            else:
                s = s + str(int(a[x]) + flag)
                flag = 0

        if flag > 0:        # 判断最后是否还有进位符
            s = s + '1'
        return s[::-1]      # 翻转返回


a = "11"
b = "1"
solution = Solution()
print(solution.addBinary(a, b))
