# https://leetcode.com/problems/climbing-stairs/


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp1 = 0
        dp2 = 1

        for x in range(n):
            temp = dp1
            dp1 = dp2
            dp2 = temp + dp2

        return dp2
