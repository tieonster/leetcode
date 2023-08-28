# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# 2 Approaches work here:
# 1) Using Bucket Sort:
# Create counts dictionary
# Create frequency list of lists
# Append items to freq array based on count in counts dict
# Loop starting from the back in freq array to get most frequent elements from bucket sort

# 2) Using Heap
# Create a counts dictionary
# Convert it to tuple and then heapify it to become max heap
# Pop from maxheap and append results into array

# Approach 1 (Using Heap)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:                
        # Heap Approach (Own Approach)
        counts = {}
        res = []
        
        # Get counts of each value in nums array
        for num in nums:
            if num not in counts:
                counts[num] = 1              
            else:
                counts[num] += 1
        
        # Convert counts to tuple for heap processing, add negative sign to value since we are using max heap
        # Heapify works on list of tuples, and orders by first element in each tuple
        count_pairs = [(-v, k) for k, v in counts.items()]
        
        heapq.heapify(count_pairs)
        
        while len(res) < k:
            maxVal = heapq.heappop(count_pairs) # Pop element that has most frequent count

            res.append(maxVal[1]) # Append element to results array
            
        return res

# Approach 2 (Using Bucket Sort Algorithm from Neetcode)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Approach (Neetcode solution)
        counts = {}
        freq = [[] for i in range(len(nums)+1)] # Increase freq list by 1 to for looping backwards later

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
          
        # Append items to freq array based on count in counts dict
        for num, count in counts.items():
            freq[count].append(num)
            
        res = []
        
        for i in range(len(freq)-1, 0, -1): # Looping backwards stops at index 1 and does not move to index 0, index 0 is always empty
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        
        
                
        
                        
            
            
        

            