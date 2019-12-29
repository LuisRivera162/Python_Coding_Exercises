# https://leetcode.com/problems/valid-parentheses/


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = "([{"
        closing = ")]}"

        stack = []

        for character in s:
            if character in opening:
                stack.append(character)

            else:
                if not (len(stack) != 0 and opening.find(stack.pop()) == closing.find(character)):
                    return False

        return len(stack) == 0

# Could've used a dictionary for faster time 
