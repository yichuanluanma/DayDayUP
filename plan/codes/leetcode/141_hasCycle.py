 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: hasCycle.py
 # author by: Lexi


 #class Solution {
 #public:
 #    bool hasCycle(ListNode *head) {
 #        ListNode* slow=head,*fast=head;
 #        while(fast&&fast->next){
 #            slow=slow->next;
 #            fast=fast->next->next;
 #            if(slow==fast)return true;
 #        }  
 #    }  
 #
 #}; 
 
 class Solution:
     def hasCycle(self, head):
         """
         :type head: ListNode
         :rtype: bool
         """
         fast = slow = head
         while fast and fast.next:
             fast = fast.next.next
             slow = slow.next
             if slow == fast:
                 return True
         return False
