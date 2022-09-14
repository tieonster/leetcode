# Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.


# Idea is to create a dummy node and a left and right pointer
# Set left and right pointer to be n nodes away from each other
# Once right pointer hits null, left pointer will be at node just before deleted node
# Set left pointer, left.next = left.next.next to delete the node
# Return dummy linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head # Want right pointer to be head + n
        
        # To make sure the right pointer is n steps away from the left pointer
        while (n > 0 and right):
            right = right.next
            n -= 1
            
        # Increment left and right pointer until reach end of last node
        while right:
            left = left.next
            right = right.next
            
        # Delete node (Dummy node gets updated as well)
        left.next = left.next.next
            
        return dummy.next
        