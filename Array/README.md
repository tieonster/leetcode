# Questions attempted:

### Best Time to buy and sell stock:
Sliding window technique with left and right pointer
Key: If left pointer has higher value than the right pointer, set left pointer as right pointer
Use max function to find maximum profit
[SOLUTION](https://www.youtube.com/watch?v=1pkOgXD63yU)

### Longest Substring Without Repeating Characters:
Create left and right pointer
Use a set to check for duplicates
[SOLUTION](https://www.youtube.com/watch?v=wiGpQwVHdE0)

### Maximum Subarray
[SOLUTION](https://www.youtube.com/watch?v=5WZl3MMT0Eg)

### Minimum Size Subarray Sum
[SOLUTION](https://www.youtube.com/watch?v=aYqYMIqZx5s)


### Product of Array Except Self
To solve this problem in O(n) time complexity without using the division operation, you can utilize two arrays: one to store the product of all elements to the left of the current element, and another to store the product of all elements to the right of the current element. Then, you can multiply these two arrays element-wise to get the final answer.
[SOLUTION](https://www.youtube.com/watch?v=bNvIQI2wAjk)

### Two Sum
Use a hashmap to store the values already iterated through
[SOLUTION](https://www.youtube.com/watch?v=KLlXCFG5TnA)

### Two Sum II
Use a 2-pointer approach

### Three Sum
Use a two pointer approach within a for loop (Two Sum and Two Sum II combined)
[SOLUTION](https://www.youtube.com/watch?v=jzZsG8n2R9A)

### Subarray Sums Divisible by k (Citadel Question)
Has some math logic involved here <br />
Basically, store the remainder of the cumSum in a separate array <br />
Sum up according to the formula provided: <br />
1) For keys with 0, increment with nC2 + n <br />
2) Rest of the keys increment with nC2 <br />
[SOLUTION](https://www.youtube.com/watch?v=u9m-hnlcydk)

### Pairs of Songs with Total Duration Divisible by 60 (Goldman Sachs)
Modulo all songs first <br />
Create hashmap with counts <br />
Increment count of new songs when looping through new songs list or hashmap (See code for both methods) <br />

### Container with Most Water
Idea is to use 2 pointers <br />
Set left and right pointers to both ends of the array <br />
Idea is to maximise the water so it is a good idea to set length of container to maximum at first <br />
Slowly increment/decrement left and right pointer based on which is smaller. <br />
[SOLUTION](https://www.youtube.com/watch?v=UuiTKBwPgAo)

### Longest Consecutive Sequence
The idea is to first populate the hash set with all the elements from the array, and then for each element, <br /> 
check if the consecutive elements are present in the hash set. This way, you can count the length <br />
of the consecutive sequence for each element. <br />
[SOLUTION](https://www.youtube.com/watch?v=P6RZZMu_maU&t=363s)

### Jump
Greedy Approach <br />
Goal is to iterate from the last element <br />
Set goal variable which contains the index of the last element <br />
Check if the index + number of jumps on the index is more than or equals to the goal index <br />
If it fulfills the criteria, it means that it is able to jump from the current index to the goal index <br />
Set goal to the current index <br />
After finishing the loop, if the goal is at index 0, it means that it is successful. <br />
Return True, else Return False <br /> 
[SOLUTION](https://www.youtube.com/watch?v=Yan0cv2cLy8)