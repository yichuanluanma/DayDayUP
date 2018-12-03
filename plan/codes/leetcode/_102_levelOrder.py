 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: levelOrder.py
 # author by: Lexi
 
 class Solution:
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         #广度优先遍历（BFS）
         #res = []
         #if root == None:
         #    return res
 
         #q = [root]
         #while len(q) != 0:
         #    res.append([node.val for node in q])
         #    new_q = []
         #    for node in q:
         #        if node.left:
         #            new_q.append(node.left)
         #        if node.right:
         #            new_q.append(node.right)
         #        q = new_q
         #return res

         #深度优先搜索（DFS）
         res = []
         self.dfs(root, 0, res)
         return res
 
     def dfs(self, root, depth, res):
         if root == None:
             return res
         if len(res) < depth + 1:
             res.append([])
             res[depth].appen(root.val)
             self.dfs(root.left, depth+1, res)
             self.dfs(root.right, depth+1, res)

