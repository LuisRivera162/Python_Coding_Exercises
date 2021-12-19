# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        
        while left <= right:
            mid = int((left+right)/2)
            
            if matrix[mid][-1] == target or matrix[mid][0] == target:
                return True
            elif matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return self.binary_search(matrix[mid], target)
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