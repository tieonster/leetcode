# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion


# Consider 3 cases:
# 1) Case where newInterval is larger than current interval, then just append current interval to res array
# 2) Case where newInterval is smaller than current interval, then just append new interval to res array, and set newInterval to current interval
# 3) Case where both intervals overlap with one another, then merge overlaps

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        if len(intervals) == 0:
            return [newInterval]
        
        # Loop through current intervals 
        for index, interval in enumerate(intervals):
            
            # Case where newInterval is greater than interval
            if interval[1] < newInterval[0]:
                res.append(interval)
                
            # Case where interval is greater than newInterval
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            
            # Case where there is overlap between interval and newInterval
            elif interval[0] <= newInterval[1] and newInterval[0] <= interval[1]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        res.append(newInterval)
        return res
        