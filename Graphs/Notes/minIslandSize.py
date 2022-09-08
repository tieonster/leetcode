from cmath import inf

def minIslandSize(grid):
    visited = set()
    minSize = inf

    # Helper DFS function to return size of array
    def dfs(grid, r, c, visited):
        # Check boundaries
        rowInbounds = 0 <= r and r < len(grid)
        colInbounds = 0 <= r and r < len(grid[0])
        if rowInbounds == False or colInbounds == False:
            return 0

        # Check if it is water
        if grid[r][c] == "0":
            return 0

        # Check if position has been visited
        position = (r, c)
        if position in visited:
            return 0
    
        visited.add(position)

        # Run dfs recursively
        size = 1
        size += dfs(grid, r-1, c, visited)
        size += dfs(grid, r+1, c, visited)
        size += dfs(grid, r, c-1, visited)
        size += dfs(grid, r, c+1, visited)

        return size

    # Main function
    for r_index, row in enumerate(grid):
        for c_index, col in enumerate(row):
            size = dfs(grid, r_index, c_index, visited)
            if size < minSize:
                minSize = size

    return minSize