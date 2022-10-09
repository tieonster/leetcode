# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to 
# remove to make the rest of the intervals non-overlapping.

# Store the ending of each interval in variable called prevEnd
# Iterate through every interval, and if they are not overlapping, update prevEnd to the value of the current interval end
# If they are overlapping, then update prevEnd to the min value of the current interval's end and previous end
# Update result by 1

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1] # Don't actually have to delete intervals, just need to store end value
        for start, end in intervals[1:]:
            if start >= prevEnd: # If not overlapping, means current interval's end is definitely larger than previous end, change prevEnd
                prevEnd = end
            else:
                prevEnd = min(end, prevEnd) # If overlapping, then only keep the interval that ends earlier
                res += 1
                
        return res