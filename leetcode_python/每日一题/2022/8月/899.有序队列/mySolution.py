'''
# @Time : 2022/8/3 9:58
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    # 注意一个规律，k==1时，依次往后添加比较最大即可
    # k > 1时，实际上就是排序

    def orderlyQueue(self, s: str, k: int) -> str:
        list1 = list(s)
        minRes = "".join(list1)
        if k == 1:
            for _ in range(len(list1)):  # 遍历移动一次
                list1.append(list1[0])
                del list1[0]
                if "".join(list1) < minRes:
                    minRes = "".join(list1)
        if k > 1:
            return ''.join(sorted(list1))

        return minRes


s = "cba"
k = 1
solution = Solution()
print(solution.orderlyQueue(s, k))
