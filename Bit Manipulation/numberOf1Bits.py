# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).


# Take the int n and find the remainder when divided by 2. If remainder is 1, then 1 exists in the last digit
# Bit shift n to the right by 1 and repeat operation until n is empty

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n: 
            res += n % 2
            n = n >> 1
            
        return res