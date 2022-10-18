# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Idea is to create an adjacency list and run a dfs on it
# Adjacency list is stored as preMap dictionary with list as values
# Create visited set to keep track of nodes visited
# In dfs function, return False if course has been visited (indicates cycle)
# return True if particular course does not have any prerequisites
# In each dfs run, loop through the values in particular key of preMap
# Returns false if dfs(prereq) is False
# Remove course from visited
# Set preMap[course] to empty list to show that it has been visited
# Else return True
# Call dfs function on each course


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create adjacency list of courses and their prerequisites
        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        # Create visited set to store courses that have been visited
        visited = set()
        
        def dfs(course):
            # Means there is a cycle
            if course in visited:
                return False
            
            if preMap[course] == []:
                return True
            
            visited.add(course)
            
            for pre in preMap[course]:
                if not dfs(pre): # If dfs(pre) returns False, then function returns False
                    return False
                
            visited.remove(course)
            preMap[course] = [] # Set particular course to empty list since we would already know that course can be completed
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
        