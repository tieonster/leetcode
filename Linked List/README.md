# Questions attempted:

### Reverse Singly Linked List
Can either use iterative or recursive approach <br />
Create and set 2 pointers correctly <br />
Drawing out pointers would be easier <br />
[SOLUTION](https://www.youtube.com/watch?v=G0_I-ZF0S38)

### Linked List Cycle
Makes use of Flloyd's Finding Cycle Algorithm <br />
Create one pointer called slow, and another called fast <br />
Increment slow by one and fast by two for each step takem <br />
The 2 pointers will meet after a while if there is a cycle <br />
If fast hits a null node first, it means there is no cycle <br />
[SOLUTION](https://www.youtube.com/watch?v=gBTe7lFR3vc)

### Merge Two Sorted Lists
Create a dummy node and a tail pointer for the dummy node <br />
Iterate through both list 1 and list 2, and pointer the tail pointer to the lower value  <br />
When finished traversing through a particular list, set the remaining of the tail.next to the remaining list not traversed yet <br />
[SOLUTION](https://www.youtube.com/watch?v=XIdigk956u0)

### Remove nth node from end of linked list
Create a dummy node, a left pointer, and a right pointer <br />
Set left and right pointer to be n nodes away from each other <br />
Once right pointer hits null, left pointer will be at node just before deleted node <br />
Set left pointer, left.next = left.next.next to delete the node <br />
Return dummy linked list <br />
[SOLUTION](https://www.youtube.com/watch?v=XVuQxVej6y8)
To find out about linked list pointers and variable assignment, refer to iPad drawing or this [link:](https://stackoverflow.com/questions/58715870/explanation-about-dummy-nodes-and-pointers-in-linked-lists) 

### Remove nth node from end of linked list
Create fast and slow pointers to find out split between linked list <br />
Reverse second half of linked list <br />
Loop and change pointers of linked list <br />
[SOLUTION](https://www.youtube.com/watch?v=S5bfdUTrKLM)

### Add Two Numbers
Solved using my own method but Neetcode provides a more efficient solution <br />
[SOLUTION](https://www.youtube.com/watch?v=wgFPrzTjm7s)
