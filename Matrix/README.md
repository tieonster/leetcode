# Questions attempted:

### Set Matrix Zeros
General Idea is to use recursion <br />
Create a function within the main function and call it recursively <br />
Continue if high pointer is more than low pointer <br />
3 conditions: <br />
If target == middle value <br />
elif target > middle value <br />
elif target < middle value <br />
[SOLUTION](https://www.youtube.com/watch?v=s4DPM8ct1pI)

### Spiral Matrix
Create rowBegin, rowEnd, colBegin, colEnd pointer <br />
While loop at the start to make sure rowBegin <= rowEnd and colBegin <= colEnd <br />
First, traverse right and increment rowBegin <br />
Next, traverse down and decrement colEnd<br />
3 conditions: <br />
Next, traverse left and decrement rowEnd (Check if rowBegin < rowEnd to handle case if matrix is non square) <br />
Lastly, traverse up and increment colBegin (Check if colBegin < colEnd to handle case if matrix is non square)<br />
Handle edge cases (e.g. if matrix is non square) <br />
[SOLUTION](https://www.youtube.com/watch?v=BJnMZNwUk1M)
