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
[SOLUTION](https://www.youtube.com/watch?v=bNvIQI2wAjk)

### Two Sum
[SOLUTION](https://www.youtube.com/watch?v=KLlXCFG5TnA)

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
Need to check whether each element in nums is the start of a sequence <br />
This can be done by iterating through each num, and then checking if the number immediately to the left of it exists <br />
If it does not exist, means it is the start of the sequence <br />
Then continue to append 1 to the length of current sequence until next number no longer exists in set. <br />
[SOLUTION](https://www.youtube.com/watch?v=P6RZZMu_maU&t=363s)