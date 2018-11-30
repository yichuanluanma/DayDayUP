 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: isSameTree.py
 # arthor by: Lexi
 
 class Solution:
     def isSameTree(self, p, q):
         """
         :type p: TreeNode
         :type 1: TreeNode
         :rtype: bool
         """
         if p == None or q == None:
             return p == q
         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
