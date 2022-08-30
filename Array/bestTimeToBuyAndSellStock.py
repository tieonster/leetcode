# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Use the sliding window technique
# left and right pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: # if left pointer has higher value than right pointer, then set left pointer to right pointer
                l = r
            r += 1
        
        return (maxP)
                