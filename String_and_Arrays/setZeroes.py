# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column_set = set()
        row_set = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    column_set.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_set or j in column_set:
                    matrix[i][j] = 0