'''
# @Time : 2022/7/19 9:29
# @Author : Admin
# @Project : PythonCode
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Node, list2: Node):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        head = Node(0)  # 创建一个新链表用于返回
        q = head
        while list1 and list2:  # 遍历
            if list1.val <= list2.val:  # 比较，较小的添加到链表中
                q.next = list1
                list1 = list1.next
            else:
                q.next = list2
                list2 = list2.next
            q = q.next  # 工作指针后移
        if list1 is None:
            q.next = list2
        if list2 is None:
            q.next = list1
        return head.next


List1 = Node(1)
List1.next = Node(5)
List1.next.next = Node(6)

List2 = Node(1)
List2.next = Node(2)
List2.next.next = Node(3)

solution = Solution()
result = solution.mergeTwoLists(List1, List2)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val, result.next.next.next.next.val, result.next.next.next.next.next.val)
