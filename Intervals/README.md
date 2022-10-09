# Notes:
This topic need to know functions to check if intervals overlap + merging intervals

### Merge Intervals
Sort intervals by starting element <br />
Loop through each interval, and check if current interval overlaps with previous interval <br />
If overlap, merge them and replace the last interval with the merged interval <br />
If not, simply add the current interval to the output <br />
[SOLUTION](https://www.youtube.com/watch?v=44H3cEC2fFM)


### Insert Interval
Assuming intervals are already sorted <br />
Loop through each interval, and consider 3 cases. <br />
Case 1: newInterval is larger than current interval, then just append current interval to res array <br />
Case 2: newInterval is smaller than current interval, then just append new interval to res array, and set newInterval to current interval <br />
Case 3: Both intervals overlap with one another, then merge overlaps <br />
[SOLUTION](https://www.youtube.com/watch?v=A8NUOmlwOlM)


### Non-overlapping Intervals
Store the ending of each interval in variable called prevEnd <br />
Iterate through every interval, and if they are not overlapping, update prevEnd to the value of the current interval end <br />
If they are overlapping, then update prevEnd to the min value of the current interval's end and previous end<br />
[SOLUTION](https://www.youtube.com/watch?v=nONCGxWoUfM)

