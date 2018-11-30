 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: isSymmetricTree.py
 # author by: Lexi
 
 class Solution:
     def isSymmetricTree(self, root):
         """
         :type root: TreeNode
         :rtype: bool
         """
         if root:
             return self.isSame(root.left, root.right)
         return True
 
     def isSame(self, p ,q):
         if p == None and q == None:
             return True
         if p and q and p.val == q.val:
             return self.isSame(p.left, q.right) and self.isSame(p.right, q.left)
         else:
             return False