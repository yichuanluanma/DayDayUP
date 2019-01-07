# coding=utf-8
class Solution:
    def removeElements(self, head, val):
        """
        :param head: ListNode
        :param val: int
        :return: ListNode
        """
        # if not head:
        #     return head
        # head.next = self.removeElements(head.next, val)
        # return head if head.val != val else head.next
        new_head = pre = ListNode(0)
        pre.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return new_head.next


