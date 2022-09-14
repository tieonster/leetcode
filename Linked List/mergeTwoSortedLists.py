# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Create a dummy node first to handle all possible edge case
# Create a pointer for this dummy node and call it tail
# while both pointers are non empty, check which list pointer has a larger value
# switch the dummy pointer to that list pointer, and switch list pointer to list.next
# At the end of each iteration of the while loop, increment the tail pointer to the next one
# Lastly, outside of the while loop, if we have traversed the entire of one of the lists, then set tail.next to be either of the one
# return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        
        while (list1 and list2):
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        tail.next = list1 or list2
                
        return dummy.next
                
            