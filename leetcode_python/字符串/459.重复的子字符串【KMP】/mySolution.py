'''
# @Time : 2022/7/28 20:52
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    # 枚举
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False

    # 枚举
    def repeatedSubstringPattern1(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i == 0:  # 必须是符合要求（可以成对）
                flag = True
                for j in range(i, length):
                    if s[j] != s[j - i]:
                        flag = False
                        break
                if flag:
                    return True
        return False

    # 匹配 （移位操作）
    def repeatedSubstringPattern2(self, s: str) -> bool:
        """
        假设母串S是由子串s重复N次而成， 则 S+S则有子串s重复2N次， 那么现在有： S=Ns， S+S=2Ns， 其中N>=2。
        如果条件成立， S+S=2Ns, 掐头去尾破坏2个s，S+S中还包含2*（N-1）s,
        又因为N>=2, 因此S在(S+S)[1:-1]中必出现一次以上

        我自己理解的是如果s不包含重复子串，那么s自己就是一次重复的子串，那么把s + s去头去尾中就一定不包含s自己。
        如果s包含重复子串，那么在s + s去头去尾中就一定能找到s自己

        """
        return (s + s).find(s, 1) != len(s)


s = "abadabad"
solution = Solution()
print(solution.repeatedSubstringPattern2(s))
