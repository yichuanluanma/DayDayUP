# coding: utf-8
"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。
示例:
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""

# 使用递归
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        self.l = []
        self.floor(root, str(root.val))
        return self.l

    def floor(self, root, path):
        if root.left == None and root.right == None:
            self.l.append(path)
        else:
            if root.left:
                self.floor(root.left, path + '->' + str(root.left.val))
            if root.right:
                self.floor(root.right, path + '->' + str(root.right.val))
