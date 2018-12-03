 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: pathSum.py
 # author by: Lexi
 class Solution:
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         if not root:
             return []
         res = []
         self.dfs(root, sum, res, [root.val])
         return res
     def dfs(self, root, target, res, path):
         if not root: return
         if sum(path) == target and not root.left and not root.right:
             res.append(path)
             return
         if root.left:
             self.dfs(root.left, target, res, path + [root.left.val])
         if root.right:
             self.dfs(root.right, target, res, path + [root.right.val])
