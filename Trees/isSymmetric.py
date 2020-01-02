# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return Solution().isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, left, right):

        if not left and right:
            return False

        if not right and left:
            return False

        if not left and not right:
            return True

        if left.val == right.val:
            l = Solution().isSymmetricHelper(left.left, right.right)
            r = Solution().isSymmetricHelper(left.right, right.left)
            return l and r
