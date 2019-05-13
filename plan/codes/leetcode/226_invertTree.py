# coding=utf-8
class Solution:
    def invertTree(self, root):
        """
        :param root: TreeNode
        :return: TreeNode
        """
        #递归（DFS）
        if root == None:
            return root
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root
