
# https://leetcode.com/problems/maximum-subarray/

import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = -sys.maxsize
        curr_sum = 0

        for number in nums:
            curr_sum += number
            if curr_sum > largest_sum:
                largest_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0

        return largest_sum
