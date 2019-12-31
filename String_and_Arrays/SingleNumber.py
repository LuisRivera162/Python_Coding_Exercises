# https://leetcode.com/problems/single-number/

import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash_set = set()

        for number in nums:
            if number in hash_set:
                hash_set.remove(number)
            else:
                hash_set.add(number)

        return hash_set.pop()