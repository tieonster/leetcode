# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.


# Similar to number of islands problem
# Use breath first search and store the max_size of islands in variable

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        max_size = 0
        
        def bfs(i, j):
            q = deque([(i,j)])
            visited.add((i,j))
            size = 1
            
            while len(q) > 0:
                curr_i, curr_j = q.popleft()
                for direction in directions:
                    next_i = curr_i + direction[0]
                    next_j = curr_j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols and (next_i, next_j) not in visited and grid[next_i][next_j] == 1:
                        q.append((next_i, next_j))
                        visited.add((next_i, next_j))
                        size += 1

            return size
            
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    size = bfs(i,j)
                    max_size = max(size, max_size)
                
        return max_size