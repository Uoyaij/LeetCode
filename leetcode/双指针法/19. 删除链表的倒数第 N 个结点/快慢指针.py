'''
# @Time : 2022/7/18 19:51
# @Author : Admin
# @Project : PythonCode
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


#  快慢指针
class Solution:
    def removeNthFromEnd(self, head: Node, n: int):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        p = slow
        for i in range(n):  # fast节点先移动n步
            fast = fast.next
        if fast is None:  # 说明删除的是第一个节点，直接返回
            return head.next
        while fast is not None:
            p = slow
            fast = fast.next
            slow = slow.next
        p.next = slow.next  # 当前slow指针指向的位置就是目标节点
        return head


head = Node(2)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(1)

solution = Solution()
result = solution.removeNthFromEnd(head, 2)
print(result.val, result.next.val, result.next.next.val)
