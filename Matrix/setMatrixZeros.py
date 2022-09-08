# Given an m x n integer matrix matrix, if an element is 0, 
# set its entire row and column to 0's.

# You must do it in place.

# Brute Force Method
# Create 2 separate arrays, one to store index of column matrix with 0 in it
# One to store index of row matrix with 0 in it

# Loop through matrix and store it in arrays

# Loop through row array and column array separately, change all values in rows and columns to 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        column_nums = []
        row_nums = []
        
        # Store column and row index containing zeros in two separate arrays
        for row_num, row in enumerate(matrix):
            column = 0
            for entry in row:
                if entry == 0:
                    column_nums.append(column)
                    if row_num not in row_nums:
                        row_nums.append(row_num)
                column += 1
        
        # Loop through row index and change all rows to 0
        for row in row_nums:
            for i, entry in enumerate(matrix[row]):
                matrix[row][i] = 0
        
        # Loop through column index and change all columns to 0
        for column in column_nums:
            for i, row in enumerate(matrix):
                matrix[i][column] = 0
                
        return matrix
                
                    
            