 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: minDepth.py
 # author by: Lexi
 
 class Solutioh:
     def minDepth(self, root):
         """
         :type root: TreeNode
         :rtype : int
         """
         if root is None:
             return 0
         if root.left == None:
             return self.minDepth(root.right) + 1
         if root.right == None:
             return self.minDepth(root.left) + 1
 
         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
