# Questions attempted:

### Combination Sum
Idea is to use a stack <br />
Create a hashmap that matches each closing bracket to its corresponding open bracket <br />
Loop through each character in the string <br />
Append it to the stack if character is opening bracket <br />
If char is closing bracket, then check to see if the last element in the stack is its corresponding opening bracket. If it is, then pop that opening bracket and continue <br />
If not return False <br />
Return true is loop is finished <br />
[SOLUTION](https://www.youtube.com/watch?v=WTzjTskDFMg)
