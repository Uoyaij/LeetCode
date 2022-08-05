'''
# @Time : 2022/7/13 10:47
# @Author : Admin
# @Project : PythonCode
'''


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print("l1:", l1)
        print("l2:", l2)
        l3 = []  # 用于返回
        flag = 0  # 标记进位
        if len(l1) > len(l2):  # 说明l1列表长
            print("len1长")
            for x in range(len(l1)):  # 遍历l1
                if x >= len(l2):  # 同时达到l2的遍历末尾
                    print("相等了")
                    print("flag值为：", flag)
                    if l1[len(l1) - x - 1] + flag >= 10:    # 只观察l1和进位值,若>=10，则进位
                        l3.append((l1[len(l1) - x - 1] + flag) % 10)
                        flag = 1
                    else:
                        l3.append(l1[len(l1) - x - 1] + flag)
                        flag = 0
                    if x == len(l1) - 1:
                        if flag == 1:
                            l3.append(flag)
                elif l1[len(l1) - x - 1] + l2[len(l2) - x - 1] + flag >= 10:  # l1和l2同时遍历且加起来的值>10,需要进位，同时设置进位值为1
                    print(">10")
                    l3.append((l1[len(l1) - x - 1] + l2[len(l2) - x - 1] + flag) % 10)
                    flag = 1
                else:  # 不超过10，进位制为0
                    print("<10")
                    l3.append(l1[len(l1) - x - 1] + l2[len(l2) - x - 1] + flag)
                    flag = 0
        else:
            print("len2长为", len(l2))
            for x in range(len(l2)):
                if x >= len(l1):
                    print("相等了")
                    print("flag值为：", flag)
                    if l2[len(l2) - x - 1] + flag >= 10:
                        l3.append((l2[len(l2) - x - 1] + flag) % 10)
                        flag = 1
                    else:
                        l3.append(l2[len(l2) - x - 1] + flag)
                        flag = 0
                    if x == len(l2) - 1:
                        if flag == 1:
                            l3.append(flag)
                elif l1[len(l1) - x - 1] + l2[len(l2) - x - 1] + flag >= 10:
                    print(">10")
                    l3.append((l1[len(l1) - x - 1] + l2[len(l2) - x - 1] + flag) % 10)
                    flag = 1
                else:
                    print("<10")
                    l3.append(l1[len(l1) - x - 1] + l2[len(l2) - x - 1] + flag)
                    flag = 0
        return l3


l2 = [9, 9, 9, 9, 9, 9, 9]
l1 = [9, 9, 9, 9]
solution = Solution()
print("res:", solution.addTwoNumbers(l1, l2))
