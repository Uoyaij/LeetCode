'''
# @Time : 2022/7/26 8:44
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
    def inorderTraversal(self, root) -> List[int]:
        """
         :param root: Optional[TreeNode]
         :return:
         """
        res = []
        stack = list()
        while root is not None or stack is not None:
            while root:
                stack.append(root)
                root = root.left
            res.append(stack[-1])
            stack.pop()
            root = root.right
        return res

    # `Morris 遍历算法是另一种遍历二叉树的方法，它能将非递归的中序遍历空间复杂度降为 O(1)O(1)。
    def inorderTraversal1(self, root) -> List[int]:
        """
        :param root: Optional[TreeNode]
        :return:
        """
        res = []
        stack = list()
        while root is not None or stack is not None:
            while root:
                stack.append(root)
                root = root.left
            res.append(stack[-1])
            stack.pop()
            root = root.right
        return res
