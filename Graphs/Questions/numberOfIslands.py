# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally 
# or vertically. You may assume all four edges of the grid are all surrounded by water.


# Uses DFS
# Trick is to come up with the main function first, and then create a function that helps with attaining main function
# Explore is the helper function in this case
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set([])
        count = 0
        
        def explore(grid, row, col, visited):
            # Makes sure row and column is not out of bounds
            rowInbounds = 0 <= row and row < len(grid)
            colInbounds = 0 <= col and col < len(grid[0])
            if rowInbounds == False or colInbounds == False:
                return False
            
            # Do not include spaces with entry 0 inside
            if (grid[row][col] == "0"):
                return False            
            
            # Acccount for visited nodes
            pos = str(row) + "," + str(col)
            if pos in visited:
                return False
            visited.add(pos)
            
            # DFS
            explore(grid, row-1, col, visited)
            explore(grid, row+1, col, visited)
            explore(grid, row, col-1, visited)
            explore(grid, row, col+1, visited)
            
            return True
        
        # Main function iterating through grid
        for r_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if explore(grid, r_index, col_index, visited) ==  True:
                    count += 1
                    
        return count



# Neetcode solution             
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
              
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    
        return islands                