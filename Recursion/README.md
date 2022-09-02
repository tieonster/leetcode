# Questions attempted:

### Generate Parantheses
General Idea is to use recursion <br />
Create a function within the main function and call it recursively <br />
Only add open parantheses if open < n <br />
Only add a closing paranthesis if closed < open <br />
If open == closed == n, then stop recursion from occurring <br />
[SOLUTION](https://www.youtube.com/watch?v=s9fokUqJ76A&t=622s)

### Combinations
General Idea is to use recursion <br />
Create a backtracking function within the main function and call it recursively <br />
Base Case of when len(comb) == k, then simply return <br />
For loop from start to n+1, within for loop, call backtracking function recursively <br />
Remember to append to comb and pop from comb respectively. <br />
[SOLUTION](https://www.youtube.com/watch?v=q0s6m7AiM7o)


### Subsets (Similar to combinations)
General Idea is to use recursion <br />
Create a backtracking function (dfs) within the main function and call it recursively <br />
Base Case of when i > len(nums) then simply return <br />
Have 2 recursive calls: <br />
First one to include the number <br />
Second one to not include the number <br />
[SOLUTION](https://www.youtube.com/watch?v=REOH22Xwdkk)

### Letter Combinations of a Phone Number
General Idea is to use recursion <br />
Create a backtracking function within the main function and call it recursively <br />
Base Case of when len(currString) == len(digits) then simply return <br />
Have to loop through mappings in each digit, and call backtrack function in each letter within the loop <br />
[SOLUTION](https://www.youtube.com/watch?v=0snEunUacZY)