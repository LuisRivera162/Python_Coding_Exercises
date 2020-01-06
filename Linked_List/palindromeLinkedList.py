# https://leetcode.com/problems/palindrome-linked-list/
# My solution is with the O(1) space challenge in mind


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        middle_head = head
        for i in range(length / 2):
            middle_head = middle_head.next

        middle_head = self.reverse(middle_head)

        temp = head
        while temp and middle_head:
            if temp.val != middle_head.val:
                return False
            temp = temp.next
            middle_head = middle_head.next

        return True


    def reverse(self, head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
