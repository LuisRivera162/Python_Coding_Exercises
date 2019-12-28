
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        curr = ""
        for character in s:
            if character in curr:
                if len(curr) > len(result):
                    result = curr
                curr = curr[curr.find(character) + 1:]

            curr = curr + character

        if len(curr) > len(result):
            result = curr

        return len(result)
