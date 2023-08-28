# Given an integer array nums, return an array answer such that answer[i] is equal to the 
# product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# ChatGPT answer
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Solution 1: Uses O(n) memory
        # You can utilize two arrays: one to store the product of all elements to the left of the current element, 
        # and another to store the product of all elements to the right of the current element. 
        # Then, you can multiply these two arrays element-wise to get the final answer.
        res = []
        n = len(nums)

        left, right = [1] * n, [1] * n

        left_product = 1
        for i in range(n):
            left[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            right[i] = right_product
            right_product *= nums[i]

        res = [left[i] * right[i] for i in range(n)]

        return res

        # Solution 2 (Uses O(1) memory, doesn't count answer array as memory complexity) --> Better
        # Simply store left and right arrays in answer directly!
        # Instead of using separate arrays to store left and right products, you can calculate them on-the-fly 
        # while constructing the final answer array. 
        # This way, you'll only need a constant amount of extra space for variables to store intermediate calculations.

        # n = len(nums)
            
        #     # Initialize the answer array with products to the left of each element
        #     answer = [1] * n
        #     left_product = 1
        #     for i in range(n):
        #         answer[i] = left_product
        #         left_product *= nums[i]
            
        #     # Calculate products to the right of each element and multiply with the answer array
        #     right_product = 1
        #     for i in range(n - 1, -1, -1):
        #         answer[i] *= right_product
        #         right_product *= nums[i]
            
        #     return answer




        