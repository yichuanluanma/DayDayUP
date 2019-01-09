# coding=utf-8
class Solution:
    def reverseList(self, head):
        """
        :param head: ListCode
        :return: ListCode
        """

        """
        通过迭代将节点重组，前面的节点转移到重组链表的后面。实际上就是头结点倒插操作。
        """
        # new_head = None
        # while head:
        #     p = head
        #     head = head.next
        #     p.next = new_head
        #     new_head = p
        # return new_head

        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev