# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    result = 0
    curr = ''

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return

        if self.isLeaf(root):
            self.curr += str(root.val)
            self.result += int(self.curr, 2)
            self.curr = self.curr[:-1]
            return

        self.curr += str(root.val)
        self.helper(root.left)
        self.helper(root.right)
        self.curr = self.curr[:-1]

    def isLeaf(self, root):
        return not root.left and not root.right
