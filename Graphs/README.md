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

# Max Area of Islands
Makes use of BFS algorithm <br />
Store max size of islands in one variable<br />
[SOLUTION](https://www.youtube.com/watch?v=iJGr1OtmH0c)

# Surrounded Regions
2 methods: <br />
First method: <br />
Find all regions using either bfs or dfs <br />
After that, in the coordinates of each of this regions, if one of them lies on the border, then it means the entire region will not be converted to "X"s <br />
If all coordinates do not contain border coordinate, then convert entire region to Xs. <br />
Second method: <br />
Transverse using dfs and capture all border coordinates that have "O" in them. Change these coordinates to "T" <br />
Transverse using for loops and convert all "O" to "X" <br />
Transverse through for loops and convert "T" back to "O" <br />
[SOLUTION](https://www.youtube.com/watch?v=9z2BunfoZ5Y)

# Course Schedule (Good adjacency list question)
Idea is to create an adjacency list and use dfs <br />
Idea is to return True or False based on whether the course can be done <br />
[SOLUTION](https://www.youtube.com/watch?v=EgI5nU9etnU)