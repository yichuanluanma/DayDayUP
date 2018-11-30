 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: maxDepth.py
 # author by: Lexi
 
 class Solution:
     def maxDepth(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if root is None:
             return 0
         if root.left == None:
             return self.maxDepth(root.right) + 1
         if root.right == None:
             return self.maxDepth(root.left) + 1
 
         return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
