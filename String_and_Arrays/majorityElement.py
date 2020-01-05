# https://leetcode.com/problems/majority-element/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash_map = {}
        for number in nums:
            if number in hash_map:
                hash_map[number] = hash_map[number] + 1
            else:
                hash_map[number] = 1

            if hash_map[number] > len(nums) / 2:
                return number
