# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Makes use of BFS algorithm
# Loop through each cell, and store coordinates of rotten oranges in queue
# Looping through q, we want to pop the rotten oranges
# Check if there are any adjacent fresh oranges beside the rotten oranges
# Append fresh orange to queue (because it will be rotten in the next time instance)
# Decrement number of fresh oranges
# Exit loop if the no. of fresh oranges == 0



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        
        # Keep track of time and number of fresh oranges left
        time, fresh = 0, 0
        
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 # Count number of fresh oranges
                if grid[r][c] == 2:
                    q.append([r,c]) # Appending coordinates of rotten oranges to queue

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)): # Loop through queue to pop all rotten oranges
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    # Don't do anything if out of bounds and not a rotten orange
                    if (row < 0 or row==len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1 ):
                        continue
                    grid[row][col] = 2 # Set fresh orange to rotten in the next time stamp
                    q.append([row, col]) # Add rotten orange to queue
                    fresh -= 1
                    
            time += 1
            
        return time if fresh == 0 else -1
                    