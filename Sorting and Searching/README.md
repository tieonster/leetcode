# Questions attempted:

### Binary Seach
General Idea is to use recursion <br />
Create a function within the main function and call it recursively <br />
Continue if high pointer is more than low pointer <br />
3 conditions: <br />
If target == middle value <br />
elif target > middle value <br />
elif target < middle value <br />
[SOLUTION](https://www.youtube.com/watch?v=s4DPM8ct1pI)

### Search in Rotated Sorted Array
Iterative Method <br />
This uses binary search since answer wants it with time complexity O(log n) <br />
Use left, middle, right pointer.<br />
while l <= r <br />
Conditions: <br />
If target == middle value, return middle value <br />
Try to search left portion, but if target is more than the middle value or target less than the extreme left number, then return l = mid + 1, can stop searching on left side. <br />
If not, set r = mid - 1 <br />
Try to search right portion, but if target is less than the middle value or target more than the extreme right number, return r = mid - 1 <br />
If not set l = mid + 1 <br />
Need to understand all the discrete cases <br />
See neetcode video solution for a better understanding <br />
[SOLUTION](https://www.youtube.com/watch?v=U8XENwh8Oy8)

### Kth smallest element in a sorted matrix
Binary Search Method <br />
Notice that top left hand corner element is smallest, bottom right hand corner element is largest<br />
Find middle of small and large.<br />
Find out numbers of elements in arrays that are less than mid between low and high. (Using bisect right function) Set variable as count <br />
if count < target, k, then set low to middle + 1 and continue in while loop <br />
else, set high to middle <br />
return low at the end <br />
[PseudoCode] (https://www.codingninjas.com/codestudio/library/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array)
[YOUTUBE SOLUTION](https://www.youtube.com/watch?v=0d6WF79hQME)