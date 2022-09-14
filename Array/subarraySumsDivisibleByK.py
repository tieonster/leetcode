
# Given an integer array nums and an integer k, 
# return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.


# Has some math logic involved here
# Basically, store the remainder of the cumSum in a separate array
# Sum up according to the formula provided:
# for keys with 0, increment with nC2 + n
# the rest of the keys increment with nC2

class Solution:
    def subarraysDivByK(self, nums: List[int],s k: int) -> int:
        # Create cumSum array
        cumSum = []
        count = 0
        for i in range(len(nums)):
            if len(cumSum) == 0:
                cumSum.append(nums[i])
                
            else:
                cumSum.append(cumSum[i-1]+nums[i])

        # Find the remainder of cumSum array at each index        
        for i in range(len(cumSum)):
            cumSum[i] = cumSum[i] % k
                
        mapping = {}

        # Create a mapping to store the remainder of each value in cumSum   
        for num in cumSum:         
            if num in mapping:
                mapping[num] += 1
            
            else:
                mapping[num] = 1

       # Increment count accordingly
       # for keys with 0, increment with nC2 + n
       # the rest of the keys increment with nC2             
        for key, value in mapping.items():
            if key == 0:
                count += math.comb(value, 2) + value
                
            else:
                count += math.comb(value, 2)
                
        return count
      
                
            
                
        
                
        
            