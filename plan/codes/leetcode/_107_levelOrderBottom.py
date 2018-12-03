 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: levelOrderBottom.py
 # author by: Lexi
 
 class Solution:
     def levelOrderBottom(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         queue = collections.deque()
         result = []
         queue.append(root)
         while queue:
             size = len(queue)
             current_list = []
             for i in range(0, size):
                 node = queue.popleft()
                 if node:
                     current_list.append(node.val)
                     queue.append(node.left)
                     queue.append(node.right)
             if current_list:
                 result.insert(0, current_list)
         return result