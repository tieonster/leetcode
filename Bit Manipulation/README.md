# Notes:
This topic need to know functions to check if intervals overlap + merging intervals

### Merge Intervals
Use XOR bitwise operation <br />
XOR every number in the array with each other to get the unique number <br />
[SOLUTION](https://www.youtube.com/watch?v=qMPX1AOa83k)

### Number of 1 bits
Use bit shifting to the right <br />
Divide number by 2 and get the remainder. If remainder = 1, means a 1 exists in the binary. <br />
Bit shift the entire thing to the right by 1 <br />
Repeat operation above and adding the 1 to the result. <br />
[SOLUTION](https://www.youtube.com/watch?v=5Km3utixwZs)