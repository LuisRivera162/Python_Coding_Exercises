# https://leetcode.com/problems/reverse-integer/


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        string = str(x)
        isNegative = False
        result = string[::-1]

        if result[len(result) - 1] == '-':
            result = result[:len(result) - 1]
            isNegative = True

        result = int(result)
        if isNegative:
            result *= -1

        if result > 2147483647 or result < -2147483647:
            return 0

        return result
