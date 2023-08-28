# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Need to check each element in nums and see if it is the start of a sequence
# To determine if it is the start of a sequence, check if the immediate number to the left and see if it exists in nums
# If it does not exist, then start checking to see if the immediate number to the right of the sequence exists, and keep appending to the length

# The idea is to first populate the hash set with all the elements from the array, and then for each element, 
# check if the consecutive elements are present in the hash set. This way, you can count the length 
# of the consecutive sequence for each element.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:  # Only start from the smallest element of a sequence
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length

## Step by step explanation ##
# The longest_consecutive function takes an unsorted array of integers nums as input.

# The initial check if not nums: ensures that if the input array is empty, the function returns 0, since there can't be any consecutive sequence in an empty array.

# A hash set called num_set is created to store the unique elements from the input array nums.

# A variable max_length is initialized to keep track of the maximum length of consecutive sequences found in the array.

# The code enters a loop that iterates through each element num in the num_set.

# Inside the loop, there's a check if num - 1 not in num_set. This check helps identify the smallest element of a consecutive sequence. If the element num - 1 is not present in the hash set, it means num is the smallest element of a potential consecutive sequence.

# If the current num is indeed the start of a sequence, then the algorithm enters another loop to find the length of the consecutive sequence. It increments current_num by 1 and increases current_length by 1 for each consecutive element found in the hash set.

# The inner loop continues as long as current_num + 1 is in the hash set, indicating that the next consecutive element is present.

# After exiting the inner loop, the max_length is updated with the maximum value between the current max_length and current_length. This ensures that we keep track of the longest consecutive sequence found so far.

# The outer loop continues iterating through all elements in the num_set, checking for potential sequences.

# Finally, the function returns the max_length, which represents the length of the longest consecutive sequence found in the input array.

            