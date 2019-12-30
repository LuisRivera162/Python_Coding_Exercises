# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0

        largest_profit = 0
        lowest = prices[0]

        for index in range(len(prices)):
            if index > 0:
                if prices[index] - lowest <= 0:
                    lowest = min(lowest, prices[index])
                else:
                    largest_profit = max(largest_profit, prices[index] - lowest)

        return largest_profit
