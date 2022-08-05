'''
# @Time : 2022/8/5 7:58
# @Author : Admin
# @Project : PythonCode
'''

import tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if root == None:
            return
        if depth == 1:  # 将root添加导新节点中
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root

    # BFS
    def addOneRow1(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root, None)
        curLevel = [root]
        for _ in range(1, depth - 1):
            tmpt = []
            for node in curLevel:
                if node.left:
                    tmpt.append(node.left)
                if node.right:
                    tmpt.append(node.right)
            curLevel = tmpt  # 记录上一层的所有节点
        for node in curLevel:  # 为该层添加节点
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root


if __name__ == "__main__":
    root = [4, 2, 6, 3, 1, 5]
    val = 1
    depth = 2
    solution = Solution()
    newTree = tree.generate_tree(root)
    res = solution.addOneRow(newTree, val, depth)

    print(tree.bfs(res))
