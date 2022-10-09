# Notes:

### K Closest Points to Origin
Use minheap heap <br />
Change distance calculated to negative number in order to make a maxheap  <br />
Pop and push item accordingly <br />
Note: Need to be familiar with the python heapq documentation, heappushpop with tuple as argument <br />
[SOLUTION](https://www.youtube.com/watch?v=rI2EBUEMfTk)

### Top K Frequent Elements (IMPORTANT)
2 Approaches <br />
1) Using Bucket Sort <br />
Create a frequency list of lists <br />
Each index represents the frequency of occurence of elements, so each index contains a list of elements <br />
After appending elements to the freq list of lists, loop from the back to append elements to results array. <br />
2) Using MaxHeap <br />
Create dictionary of counts and convert it to tuple <br />
Convert dictionary to maxheap and pop elements based on frequency of occurence into res array. <br />
[SOLUTION](https://www.youtube.com/watch?v=YPTqKIgVk-k)
