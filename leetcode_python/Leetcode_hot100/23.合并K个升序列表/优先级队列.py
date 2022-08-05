'''
# @Time : 2022/7/20 13:19
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
        import heapq  # 导入堆库
        head = Node(0)
        p = head     # 工作指针
        res = []
        for i in range(len(lists)):     # 遍历链表数组
            q = lists[i]
            while q:
                heapq.heappush(res, q.val)  # 压入到小顶堆中（压入值和对应的数组索引）
                q = q.next

        for i in range(len(res)):
            val = heapq.heappop(res)    # 取值
            p.next = Node(val)      # 构建添加节点
            p = p.next          # 工作指针后移
        return head.next


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
