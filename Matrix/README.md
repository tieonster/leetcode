# Questions attempted:

### Set Matrix Zeros
Create two separate arrays to store index of rows containing zeroes and columns containing zeroes <br />
Iterate through matrix rows and change all rows containing 0 to 0. <br />
Iterate through matrix columns and change all columns containing 0 to 0. <br />
[SOLUTION](https://www.youtube.com/watch?v=T41rL0L3Pnw)

### Spiral Matrix
Create rowBegin, rowEnd, colBegin, colEnd pointer <br />
While loop at the start to make sure rowBegin <= rowEnd and colBegin <= colEnd <br />
First, traverse right and increment rowBegin <br />
Next, traverse down and decrement colEnd<br />
Next, traverse left and decrement rowEnd (Check if rowBegin < rowEnd to handle case if matrix is non square) <br />
Lastly, traverse up and increment colBegin (Check if colBegin < colEnd to handle case if matrix is non square)<br />
Handle edge cases (e.g. if matrix is non square) <br />
[SOLUTION](https://www.youtube.com/watch?v=BJnMZNwUk1M)
