# https://leetcode.com/problems/move-zeroes/


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums

        pointer = 0

        for index in range(len(nums)):
            if nums[index] != 0:
                nums[pointer] = nums[index]
                if index != pointer:
                    nums[index] = 0
                pointer += 1

        return nums
