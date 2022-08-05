'''
# @Time : 2022/7/14 9:59
# @Author : Admin
# @Project : PythonCode
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: Node, l2: Node):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = Node(0)  # 指针节点
        head = l1  # 指向l1,用于返回
        p = l1  # 指针节点
        flag = 0  # 进位数
        while l1 or l2:  # l1或l2链表存在
            n1 = (l1.val if l1 else 0)  # 如果l1有数据，则n1为该数据，否则为0
            n2 = (l2.val if l2 else 0)  # 如果l2有数据，则n2为该数据，否则为0
            sum = n1 + n2 + flag  # 值相加
            if p:  # 修改l1上链表的值
                p.val = sum % 10
                r = p  # r标记p
                p = p.next  # p向后移动
            else:  # p不存在
                r.next = Node(0)  # 为l1创建新节点
                r.next.val = sum % 10
                r.next.next = None
                r = r.next
            flag = int(sum / 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if flag > 0:  # 最后的进位值>0加入到链表中
            r.next = Node(0)
            r.next.val = flag
            r.next.next = None
        return head


num1 = Node(2)
num1.next = Node(4)
num1.next.next = Node(3)

num2 = Node(5)
num2.next = Node(6)
num2.next.next = Node(4)

solution = Solution()
result = solution.addTwoNumbers(num1, num2)
print(result.val, result.next.val, result.next.next.val)
