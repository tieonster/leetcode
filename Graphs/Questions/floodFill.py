# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.


# My own solution using BFS (adapted from Neetcode numberOfIslands problem)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        coordinates = []
        rows, cols = len(image), len(image[0])

        # BFS implementation iterative
        q = collections.deque()
        visited.add((sr,sc))
        q.append((sr,sc))

        while q:
            row, col = q.popleft() # Change this to pop to implement DFS
            directions = [[1,0] , [-1, 0], [0, 1], [0, -1]] # Directions to traverse in
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and c in range(cols) and image[r][c] == image[sr][sc] and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))
                    coordinates.append((r,c))
        
        # Change all the pixel colours according to coordinates saved
        for r, c in coordinates:
            image[r][c] = color
        
        # Always change the starting pixel to the desired colour
        image[sr][sc] = color
        
        return image
        