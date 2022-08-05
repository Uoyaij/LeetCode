'''
# @Time : 2022/7/27 14:31
# @Author : Admin
# @Project : PythonCode
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        pre = head
        p = pre.next
        while p:
            if p.val == val:
                pre.next = p.next  # 删除元素
                p = p.next
            else:
                pre = p
                p = p.next
        return head

    # 递归
    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        head.next = self.removeElements1(head.next, val)
        return head.next if head.val == val else head


num = ListNode(1)
# num.next = ListNode(2)
# num.next.next = ListNode(3)

solution = Solution()
res = solution.removeElements1(num, 1)
print(res)
