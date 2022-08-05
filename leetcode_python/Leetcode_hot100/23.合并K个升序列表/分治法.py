'''
# @Time : 2022/7/20 11:42
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Node]):
        """
        :param lists: List[ListNode]
        :return: Node
        """
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):  # 递归算法，进行两条链表的合并
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



num = None

num1 = Node(1)
num1.next = Node(4)
num1.next.next = Node(5)

num2 = Node(1)
num2.next = Node(3)
num2.next.next = Node(4)

num3 = Node(2)
num3.next = Node(6)

list = [num1, num2]
solution = Solution()
res = solution.mergeKLists(list)
print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val)
