# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Create a prev node
# Set current node to head
# Set head to head.next
# Set curr.next to prev
# Set prev node to curr node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # Create 2 pointers
        while curr: # While head is not empty
            nxt = curr.next # Temporary variable
            curr.next = prev # Set head to next node

            # Move pointers
            prev = curr # Set next node to prev
            curr = nxt # Set prev node to current
            
        return prev
            
            