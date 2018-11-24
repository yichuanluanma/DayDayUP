 #!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: mergeTwoLists.py
 # author by: Lexi
 
 class Solution:
     def mergeTwoLists(self, l1, l2):
         """
         :type l1: ListNode
         :type l2: ListNode
         :rtype: ListNode
         """
         #递归
         #if l1 == None:
         #    return l2
         #if l2 == None:
         #    return l1
         ##创建一个新链表，此为头结点
         #head = ListNode(0)
         #if l1.val < l2.val:
         #    head = l1
         #    head.next = self.mergeTwoLists(l1.next, l2)
         #else:
         #    head = l2
         #    head.next = self.mergeTwoList(l1, l2.next)
         #return head

         l = list()
         while(l1!=None):
             l.append(l1.val)
             l1 = l1.next
         while(l2!=None):
             l.append(l2.val)
             l2 = l2.next
         return sorted(l)

