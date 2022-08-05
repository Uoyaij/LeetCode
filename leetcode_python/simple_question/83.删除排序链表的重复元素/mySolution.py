'''
# @Time : 2022/7/25 10:09
# @Author : Admin
# @Project : PythonCode
'''


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    # 快慢指针
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = head
        rpre = head
        q = r = pre.next
        while q:
            if q.val != pre.val:
                r.val = q.val
                q = q.next
                pre = pre.next
                rpre = r
                r = r.next
            else:
                q = q.next
                pre = pre.next
        rpre.next = None
        return head

num1= ListNode(2)

num = ListNode(1)
num.next = ListNode(1)
num.next.next = ListNode(2)
num.next.next.next = ListNode(3)
num.next.next.next.next = ListNode(7)

solution = Solution()
solution.deleteDuplicates(num1.next)
print(num)
