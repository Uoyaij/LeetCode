'''
# @Time : 2022/7/27 20:38
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in magazine:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for j in ransomNote:
            if j not in dict:
                return False
            else:
                dict[j] -= 1
                if dict[j] < 0:
                    return False
        return True


ransomNote = "a"
magazine = ""
solution = Solution()
print(solution.canConstruct(ransomNote, magazine))
