# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.



# Flloyd's Finding Cycle Algorithm
# Create one pointer called slow, and another called fast
# Increment slow by one and fast by two for each step takem
# The 2 pointers will meet after a while if there is a cycle
# If fast hits a null node first, it means there is no cycle



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        if head == None:
            return False
        
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False