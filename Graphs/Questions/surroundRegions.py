# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# There are 2 solutions.
# The first solution is more brute force.
# Find all regions
# After that, in the coordinates of each of this regions, if one of them lies on the border, then it means the region will not be converted to Xs
# If all coordinates do not contain border coordinates, then convert entire region to Xs

# Neetcode solution:
# Reverse Thinking

# 1) Transverse using dfs and capture all border coordinates that have "O" in them. Change these coordinates to "T"
# 2) Transverse using for loops and convert all "O" to "X"
# 3) Transverse through for loops and convert "T" back to "O".

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # My own solution
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def bfs(i, j):
            coordinates = [(i,j)]
            q = deque([(i,j)])
            visited.add((i,j))
            res = True
            
            while q:
                curr_i, curr_j = q.popleft()
 
                for direction in directions:
                    next_i = curr_i + direction[0]
                    next_j = curr_j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols and (next_i, next_j) not in visited and board[next_i][next_j] == "O":
                        coordinates.append((next_i, next_j))
                        q.append((next_i, next_j))
                        visited.add((next_i, next_j))
            
            for x,y in coordinates:
                if x == 0 or x == rows-1:
                    res = False
                    break
                if y == 0 or y == cols-1:
                    res = False
                    break
                
            return coordinates, res
                        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    coordinates, res = bfs(i,j)
                    if res:
                        for x, y in coordinates:
                            board[x][y] = "X"     
                    
        return board


# Neetcode Solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
# Neetcode method
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
# 1. DFS Capture unsurrounded regions (O -> T)
        def dfs(i, j):
            board[i][j] = "T"
            
            visited.add((i,j))
            
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and board[next_i][next_j] == "O" and board[next_i][next_j] not in visited:
                    dfs(next_i, next_j)
                    
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and board[i][j] == "O":
                    if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                        dfs(i, j)

# 2. Convert remaining (O -> X)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

# 3. Uncapture unsurrounded regions (T -> O)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
                    
        return board

                
        
                       
        
        