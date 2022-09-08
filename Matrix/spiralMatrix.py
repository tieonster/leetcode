# Given an m x n matrix, return all elements of the matrix in spiral order.

# First, traverse right and increment rowBegin
# Next, traverse down and decrement colEnd
# Next, traverse left and decrement rowEnd
# Lastly, traverse up and increment colBegin

# Edge case is if when you traverse left or up, check whether the col or row still exists to prevent duplicates.
# This handles the case of a non square matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowBegin = 0
        rowEnd = len(matrix) - 1
        columnBegin = 0
        columnEnd = len(matrix[0]) - 1
        
        res = []
        
        while rowBegin <= rowEnd and columnBegin <= columnEnd:
            
            # Traverse through first row right
            for i in range(columnBegin, columnEnd+1):
                res.append(matrix[rowBegin][i])
            
            rowBegin += 1
                
            # Traverse through column down
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][columnEnd])
            
            columnEnd -= 1
            
            # Handle case is if matrix columns > rows
            if rowBegin <= rowEnd:
                # Traverse through row left
                for i in range(columnEnd, columnBegin-1, -1):
                    res.append(matrix[rowEnd][i])
            
            rowEnd -= 1
            
            # Handle case if matrix rows > columns
            if columnBegin <= columnEnd:
                # Traverse through column up
                for i in range(rowEnd, rowBegin-1, -1):
                    res.append(matrix[i][columnBegin])

            columnBegin += 1
            
        return res
                
            
                    