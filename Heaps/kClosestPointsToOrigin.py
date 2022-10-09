# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Idea is to use a heap of fixed length k in order to push and pop elements into heap

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculateDistance(x,y):
            return (x**2) + (y**2)
        
        heap = []
        # Convert array to heap
        heapq.heapify(heap)
        
        for point in points:
            # Negative sign to convert minheap to maxheap
            distance = -calculateDistance(point[0], point[1])
            
            # Controls length of min heap
            if len(heap) == k:
                # push item into heap, then pop smallest item (highest negative number)
                heapq.heappushpop(heap, (distance, point[0], point[1]))
                    
            else:
                # push item into heap
                heapq.heappush(heap, (distance, point[0], point[1]))
        
        return [[x,y] for (dist,x, y) in heap]
        
        
            
        
        
            