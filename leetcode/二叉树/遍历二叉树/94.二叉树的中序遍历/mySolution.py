'''
# @Time : 2022/7/29 17:37
# @Author : Admin
# @Project : PythonCode
'''
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.travel(res, root)
        return res

    def travel(self, res, root):
        if root != None:
            self.travel(res, root.left)
            res.append(root.val)
            self.travel(res, root.right)

    def inorderTraversal1(self, root: [TreeNode]) -> List[int]: #左中右
        res = []
        stack = list()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
        return res
