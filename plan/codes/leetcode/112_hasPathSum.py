 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: hasPathSum.py
 # author by: Lexi
 
 class Solution:
     def hasPathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: bool
         """
         if not root :
             return False
         t = sum - root.val
         if t==0 and root.left == None and root.right == None:
             return True
         return self.hasPathSum(root.left, t) or self.hasPathSum(root.right, t)
