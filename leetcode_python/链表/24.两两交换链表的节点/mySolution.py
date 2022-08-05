'''
# @Time : 2022/7/27 15:55
# @Author : Admin
# @Project : PythonCode
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 不修改节点内部值

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)   # 虚拟头节点
        pre = res
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # swap
            cur.next = post.next
            post.next = cur
            pre.next = post
            # swap down， update pre
            pre = pre.next.next
        return res.next

    # 递归
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next     # 指向第二个节点
        head.next = self.swapPairs(newHead.next)  # 让第一个节点指向后续节点
        newHead.next = head     # 翻转
        return newHead
