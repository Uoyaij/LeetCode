'''
# @Time : 2022/7/18 19:14
# @Author : Admin
# @Project : PythonCode

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: Node, n: int):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head  # 工作指针
        length = 0
        while p is not None:  # 求出链表长度
            p = p.next
            length = length + 1
        x = length - n + 1  # 转化为正序第x个节点
        p = head  # 工作指针
        r = p
        if x == 1:  # 处理头节点
            return head.next
        for i in range(x-1):
            r = p     # 指向被删除节点的前继节点
            p = p.next  # 指向被删除节点
        r.next = p.next  # 删除目标节点
        return head


head = Node(2)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(1)

solution = Solution()
result = solution.removeNthFromEnd(head, 1)
print(result.val, result.next.val, result.next.next.val)
