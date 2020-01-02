# https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        node_set = set()

        tempA = headA
        tempB = headB

        while tempA:
            node_set.add(tempA)
            tempA = tempA.next

        while tempB:
            if tempB in node_set:
                return tempB
            tempB = tempB.next

        if not tempA and not tempB:
            return None

        while headA:
            if headA in node_set:
                return headA
            headA = headA.next

        return None
