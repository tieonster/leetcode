# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Approach:
# Have a hashmap for every row and col visited, with key as the row/col number, and the value as a set
# Have a hashmap for the 3x3 square cells, with key as a tuple (r//3, c//3), and value as a set
# This 3x3 hashmap has keys which contains the coordinates of the smaller 3x3 square
# Loop through each element, and for every iteration of loop, add the value to the 3 hashmaps
# Return True after entire loop

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r // 3, c // 3) -> Convert 9x9 grid into 3x3 grid

        # Loop through rows and cols
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3, j//3)]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])

        return True
