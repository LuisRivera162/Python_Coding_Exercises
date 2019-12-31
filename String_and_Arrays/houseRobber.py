# https://leetcode.com/problems/house-robber/


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        previous = 0
        max_profit = 0

        for value in nums:
            temp = max_profit
            max_profit = max(previous + value, max_profit)
            previous = temp

        return max_profit