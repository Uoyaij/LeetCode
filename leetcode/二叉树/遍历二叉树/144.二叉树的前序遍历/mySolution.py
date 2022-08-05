'''
# @Time : 2022/7/29 16:42
# @Author : Admin
# @Project : PythonCode
'''

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> List[int]:
        res = []
        self.travel(res, root)
        return res

    def travel(self, res, root):
        if root != None:
            res.append(root.val)
            self.travel(res, root.left)
            self.travel(res, root.right)

    # 迭代
    def preorderTraversal1(self, root: TreeNode) -> List[int]:  #中左右
        res = list()
        if not root:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res
