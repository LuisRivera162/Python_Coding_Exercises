# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        temp = ListNode(0)
        dummy.next = temp

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    temp = temp.next
                    l1 = l1.next

                else:
                    temp.next = l2
                    temp = temp.next
                    l2 = l2.next

            if l1 and not l2:
                temp.next = l1
                break

            if l2 and not l1:
                temp.next = l2
                break

        return dummy.next.next
