'''
# @Time : 2022/7/27 16:27
# @Author : Admin
# @Project : PythonCode
'''


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA  # 工作指针
        q = headB
        num1 = 0  # 计算长度，用于对齐
        num2 = 0
        while p:
            num1 += 1
            p = p.next
        while q:
            num2 += 1
            q = q.next
        x = abs(num1 - num2)
        p = headA
        q = headB
        if num1 > num2:  # 对齐操作
            while x > 0:
                p = p.next
                x -= 1
        elif num2 > num1:
            while x > 0:
                q = q.next
                x -= 1
        while p and q:
            if p.val == q.val:  # 找到相交节点    去掉Val比较指针相等
                return p
            else:
                p = p.next
                q = q.next
        return p  # 没找到，返回None

    # 双指针
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        if not headA:
            return headA
        if not headB:
            return headB
        cur_a, cur_b = headA, headB  # 用两个指针代替a和b

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB  # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA  # 同理，b走完了就切换到a

        return cur_a
