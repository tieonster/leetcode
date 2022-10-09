# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Create fast and slow pointers to find out split point for linked list
# Reverse second half of linked list
# Loop and change pointers of linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Create slow and fast pointer to find out the point where we should split the linked list
        slow, fast = head, head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None # To split the half of the list
        prev = None # Create variable to reverse list
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        first, second = head, prev
        while second: # Use second since second linked list is smaller
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
        
            
            
            
        