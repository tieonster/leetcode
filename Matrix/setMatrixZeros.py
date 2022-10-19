class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         column_nums = []
#         row_nums = []
#         row_zeroes = [0] * len(matrix)
        
#         for row_num, row in enumerate(matrix):
#             column = 0
#             for entry in row:
#                 if entry == 0:
#                     column_nums.append(column)
#                     if row_num not in row_nums:
#                         row_nums.append(row_num)
#                 column += 1
                
#         print(row_nums)
#         print(column_nums)
        
#         for row in row_nums:
#             matrix[row] = col_zeroes
                
#         for column in column_nums:
#             for i, row in enumerate(matrix):
#                 matrix[i][column] = 0
                
#         return matrix
    
        # Neetcode solution
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows/cols need to be zeroed
        for r in range(ROWS):
            for c in range (COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Skip first row and first column since we are using first row and first column as checkers
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # If top right hand corner number is 0, it means that whole column is zero
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
                
        return matrix
        
                
                
                    
            