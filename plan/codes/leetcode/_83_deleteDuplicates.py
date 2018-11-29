 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: deleteDumplicates.py
 # author by: Lexi
 
 class Solution:
     def deleteDuplicates(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         if not head:
             return head
         b = head
         n = head.next
         while n!= None:
             if b.val != n.val:
                 b = n
                 n = n.next
             else:
                 b.next = n.next
                 n = n.next
         return head
