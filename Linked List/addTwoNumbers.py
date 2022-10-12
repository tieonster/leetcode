# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Make use of multiplier
# Loop through both linked lists
# Find total sum
# Then create new linked list and store this total sum inside the linked list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier1, multiplier2 = 1, 1
        num1, num2 = 0, 0
        
        # Loop through first linked list and get the sum of the numbers
        while l1:
            num = l1.val
            num *= multiplier1
            num1 += num
            multiplier1 *= 10
            l1 = l1.next

        # Loop through second linked list and get the sum of the numbers    
        while l2:
            num = l2.val
            num *= multiplier2
            num2 += num
            multiplier2 *= 10
            l2 = l2.next
            
        # Evaluate the total sum, convert int to string and reverse entire string
        totalSum = str(num1 + num2)[::-1]
        
        # Create a new dummy node, and set the pointer curr to the start of this dummy node
        dummy = ListNode(0)
        curr = dummy
        
        # Create new nodes and append it to the dummy node
        for i in range(len(totalSum)):
            curr.next = ListNode(totalSum[i]) 
            curr = curr.next
            
        return dummy.next
        
        
            
        
        
            