'''
# @Time : 2022/7/29 18:25
# @Author : Admin
# @Project : PythonCode
'''


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    # 递归
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.travel(root, res)
        return res

    def travel(self, root, res):
        if root:
            res.append(root.val)
            for ch in root.children:
                self.travel(ch, res)

    # 迭代
    def preorder1(self, root: 'Node') -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                for i in root.children:
                    stack.append(i)
        return res
