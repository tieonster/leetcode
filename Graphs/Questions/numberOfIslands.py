# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally 
# or vertically. You may assume all four edges of the grid are all surrounded by water.


# Uses DFS
# Trick is to come up with the main function first, and then create a function that helps with attaining main function
# Explore is the helper function in this case
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(i, j):
            q = deque([(i,j)])
            visited.add((i,j))
            
            while len(q) > 0:
                curr_i, curr_j = q.popleft()
                
                for direction in directions:
                    next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                    if (0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == "1" and (next_i, next_j) not in visited):
                        q.append((next_i, next_j))
                        visited.add((next_i, next_j))
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    islands += 1
                    
        return islands
        
        
        

                   