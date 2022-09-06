#Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).


# Can use brute force way but not recommended

# Use binary search approach
# Notice that top left hand element is the smallest, and bottom right element is the largest
# Count the number of elements that are lesser than middle element
# If count < target, k, then set low to middle + 1 and search upper bound
# else, set high to middle

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
                    
        if k == 1:
            return(matrix[0][0])
        
        # lowest number in the matrix is always the number at the top left hand corner
        low = matrix[0][0]
        # highest number in the matrix is always the number at the bottom right hand corner
        high = matrix[n-1][n-1]
        
        while (low < high):
            middle = (low + high) // 2 # Random middle number
            count = 0
            
            # Counting the number of elements in the arrays that are lesser than mid between low and high
            for i in range(n):
                x = bisect_right(matrix[i], middle)
                count += x
                
            # if number of such element is less than k, narrow the search range by increasing low value
            if count < k:
                low = middle + 1
            
            # if number of such elements is greater or equal to k, narrow the search range by decreasing high value
            else:
                high = middle;
                
        return low
        
            