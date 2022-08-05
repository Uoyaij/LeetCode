'''
# @Time : 2022/7/27 15:22
# @Author : Admin
# @Project : PythonCode
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = head
        q = head.next
        while q:
            r = q.next  # 标记
            q.next = p  # 头插入
            p = q  # 标记头插入位置
            q = r  # 跟踪
        head.next = None
        return p

    # 递归
    def reverseList1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return newHead

    def reverseList2(self, head: ListNode) -> ListNode:

        def reverse(pre, cur):
            if not cur:
                return pre

            tmp = cur.next
            cur.next = pre

            return reverse(cur, tmp)

        return reverse(None, head)

num = ListNode(1)
num.next = ListNode(2)
num.next.next = ListNode(3)
solution = Solution()
res = solution.reverseList1(num)
print(res.val, res.next.val, res.next.next.val)
