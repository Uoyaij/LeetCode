'''
# @Time : 2022/7/26 20:28
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = list()
        stack2 = list()
        for i in range(len(s)):
            if s[i] != '#':
                stack1.append(s[i])
            else:
                if stack1:
                    stack1.pop()
        for j in range(len(t)):
            if t[j] != '#':
                stack2.append(t[j])
            else:
                if stack2:
                    stack2.pop()
        return "".join(stack1) == "".join(stack2)

    def backspaceCompare1(self, S: str, T: str) -> bool:  # 双指针
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0  # skip 表示当前待删除的字符的数量

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1  # 清除字符
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:    # 退格后不一致
                    return False
            elif i >= 0 or j >= 0:  # 有一个被全部清除。
                return False
            i -= 1
            j -= 1

        return True


s = 'ab###'
r = 'c#c#c'
solution = Solution()
print(solution.backspaceCompare(s, r))
