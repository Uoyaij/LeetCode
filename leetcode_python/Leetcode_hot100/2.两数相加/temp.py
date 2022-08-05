'''
# @Time : 2022/7/14 10:36
# @Author : Admin
# @Project : PythonCode
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # 你可以实现一些链表的增删等操作


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)  # result是一个头指针，将其数据初始化为了0
        r = result  # r总是指向返回结果的链表的新元素
        carry = 0  # carry表示进位

        # 循环进行对应位相加
        while (l1 or l2):
            x = (l1.val if l1 else 0)  # 如果l1有数据，则x为该数据，否则为0
            y = (l2.val if l2 else 0)  # 如果l2有数据，则y为该数据，否则为0
            s = carry + x + y

            carry = s // 10  # 得到进位（0或1）
            r.next = ListNode(s % 10)  # 新建一个节点，并保存该位的运算结果
            r = r.next  # r与r.next将指向同一个内存地址

            # 将“指针”向后移动
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        # 判断最高位相加后是否有进位，有进位则新建一个节点保存进位‘1’
        if (carry > 0):
            r.next = ListNode(1)

        return result.next  # 注意：这里返回的是result.next，而不是result。因为result是头指针，没有真正保存有效的数据


num1 = ListNode(2)
num1.next = ListNode(4)
num1.next.next = ListNode(3)

num2 = ListNode(5)
num2.next = ListNode(6)
num2.next.next = ListNode(4)

solution = Solution()
result = solution.addTwoNumbers(num1, num2)
print(result.val, result.next.val, result.next.next.val)
