
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution(object):

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1:
            return s

        result_string = ""

        for index in range(len(s) - 1):
            even = self.helper(s, index, index)
            odd = self.helper(s, index, index + 1)

            if len(even) > len(result_string):
                result_string = even

            if len(odd) > len(result_string):
                result_string = odd

        return result_string

    def helper(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        return s[left + 1:right]

# Inspired by https://leetcode.com/problems/longest-palindromic-substring/discuss/461877/Cleanest-Python-O(n2)-Time-O(1)-Space-Solution
# was close to solving but didn't know how to manage odd/even palindromes
