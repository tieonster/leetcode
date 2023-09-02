# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Backtracking approach
# Have dfs function, which takes one input to keep track of current length of word
# Need to have a path set to keep track of paths visited so far
# if current iteration, i is same length as word, return True
# if r < 0, c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r,c) in path, return False
# if not add to current path, and do dfs
# remove path after that

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])
        path = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        print(cols)
        
        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r,c) in path):
                return False

            path.add((r,c))
            # print(path)
            res = False
            for direction in directions:
                next_r = r + direction[0]
                next_c = c + direction[1]
                res = res or dfs(next_r, next_c, i + 1)
            path.remove((r,c))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): return True

        return False

