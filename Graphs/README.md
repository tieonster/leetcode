# Questions attempted:

### Number of Islands
Implement DFS function <br />
Come up with main function, then think of secondary function <br />
First, loop through the matrix iteratively <br />
For each entry, call the explore function (DFS function) <br />
Explore function returns true or false depending on whether end node (all surrounding lands) have been explored <br />
Within explore function, have a few cases that returns false: <br/>
1) When index of row > len(grid) or index of col > len(grid[0]) <br />
2) When entry is "0" (Signifies water) <br />
3) When entry has been visited (Have an array to account for visited nodes<br />
After that, call explore function recursively, making sure to explore top, bottom, left and right subsequently. <br />
Return true at the end of the explore function <br />

### Flood Fill
Implement either BFS/DFS function <br />
Very similar to Number of Islands Problem above <br />
Just that you do not have to iterate over every single cell and they've provided you with a single cell <br />
No solution will be posted as Neetcode didn't supply any :/ <br />

# Rotten Oranges
Makes use of BFS algorithm <br />
Store rotten oranges in queue and pop them one by one <br />
Keep track of time and fresh oranges to exit loop <br />