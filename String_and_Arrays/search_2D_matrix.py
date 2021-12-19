# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return self.binary_search(matrix[i], target)
        return False
    
    def binary_search(self, list, target):
        left = 0
        right = len(list)-1
        
        while left <= right:
            mid = int((left+right)/2)
            
            if list[mid] == target:
                return True
            elif list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False