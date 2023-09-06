# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion


# Consider 3 cases:
# 1) Case where newInterval is smaller than current array, then just append newInterval to res and exit for loop
# 2) Case where newInterval is larger than current interval, then just append current to res array
# 3) Case where both intervals overlap with one another, merge overlaps, but don't append anything
# After for loop is completed, append the newInterval to res to make sure that overlapped interval gets appended

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeIntervals(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        res = []
        
        for i, interval in enumerate(intervals):
            
            # If new interval has the second number smaller than the current interval first number
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]

            # If the new interval has the 1st number larger than the current interval second number
            elif newInterval[0] > interval[1]:
                res.append(interval)

            else:
                # Set newInterval to new value after merging so that you can compare this new interval
                newInterval = mergeIntervals(interval, newInterval)
            
        res.append(newInterval)

        return res
            
        