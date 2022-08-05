'''
# @Time : 2022/7/27 18:48
# @Author : Admin
# @Project : PythonCode
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

head = ListNode(0)
head.next = ListNode(0)

solution = Solution()
print(solution.hasCycle(head))
