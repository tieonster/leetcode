# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Sort intervals by starting element
# Loop through each interval, and check if current interval overlaps with previous interval
# If overlap, merge them and replace the last interval with the merged interval 
# If not, simply add the current interval to the output

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by starting element first
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        # store results into output, and put first interval inside output
        output = [sorted_intervals[0]]
        
        # Loop through intervals
        for start, end in sorted_intervals[1:]:
            lastEnd = output[-1][1] # Get ending element of last interval in output
            lastStart = output[-1][0] # Get starting element of last interval in output
            
            # Check if current interval overlaps with previous interval, and replace last interval in output with merged interval
            if start <= lastEnd and lastStart <= end:
                output[-1] = [min(start, lastStart), max(end, lastEnd)]
            
            # If no overlap, just append current interval to output
            else:
                output.append([start, end])
                
        return output
            
    
        
            