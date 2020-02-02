# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # set solution:
        #         hash_set = set()
        #         dummy = head
        #         while dummy:
        #             if dummy in hash_set:
        #                 return True
        #             hash_set.add(dummy)
        #             dummy = dummy.next

        #         return False

        # constant space solution:
        dummy = head
        if dummy:
            dummy2 = head.next
        else:
            return False

        while dummy and dummy2:
            if dummy == dummy2:
                return True
            dummy = dummy.next
            dummy2 = dummy2.next
            if dummy2:
                dummy2 = dummy2.next
        return False
