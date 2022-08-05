'''
# @Time : 2022/7/19 10:33
# @Author : Admin
# @Project : PythonCode
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 递归法
    def mergeTwoLists(self, list1: Node, list2: Node):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2


List1 = Node(1)
List1.next = Node(5)
List1.next.next = Node(6)

List2 = Node(1)
List2.next = Node(2)
List2.next.next = Node(3)

solution = Solution()
result = solution.mergeTwoLists(List1, List2)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val, result.next.next.next.next.val,
      result.next.next.next.next.next.val)
