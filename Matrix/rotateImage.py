# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# My solution approach
# Switch the rows up and down
# If you have n rows, switch the first row and the nth row. Switch the 2nd row with the (n-1)th row
# Transpose the matrix after that

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # My Solution
        def transposeMatrix(matrix):
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Switch the rows up and down
        for i in range(len(matrix)//2):
            temp = matrix[i]
            end_row = len(matrix) - 1 - i
            matrix[i] = matrix[end_row]
            matrix[end_row] = temp

        # Transpose matrix
        transposeMatrix(matrix)

        
        # Neetcode solution
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # Save the top left
                topLeft = matrix[top][l + i]

                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1


        
