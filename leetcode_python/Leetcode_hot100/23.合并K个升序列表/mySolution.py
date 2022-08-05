'''
# @Time : 2022/7/20 10:10
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

        def merge(res: Node, newList: Node):  # 递归合并
            if not res:
                return newList
            if not newList:
                return res
            if res.val < newList.val:
                res.next = merge(res.next, newList)
                return res
            else:
                newList.next = merge(res, newList.next)
                return newList

        length = len(lists)
        if not length:
            return None
        res = lists[0]
        print("a", res.val, res.next.val, res.next.next.val)
        for i in range(1, length):
            res = merge(res, lists[i])  # 合并
        return res  # 从第二个节点返回


num = None

num1 = Node(1)
num1.next = Node(4)
num1.next.next = Node(5)

num2 = Node(1)
num2.next = Node(3)
num2.next.next = Node(4)

num3 = Node(2)
num3.next = Node(6)

list = [num1, num2, num3]
solution = Solution()
res = solution.mergeKLists(list)
print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val)
