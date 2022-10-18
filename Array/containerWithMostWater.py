# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Idea is to use 2 pointer approach
# Set left and right pointers to both ends of the array since the idea is to maximise the amount of water
# Slowly increment/decrement left and right pointer respectively based on which one is smaller

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        
        while r > l:
            length = r - l
            currHeight = min(height[l], height[r])
            area = currHeight * length
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
                
            else:
                r -= 1
            
        return res
            