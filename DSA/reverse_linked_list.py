# reverse_linked_list.py
#!/usr/bin/env python3

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    # start w this
    prev_node = None
    curr = head
    
    while curr:
        next_node = curr.next # save ref to next node
        if curr.next:
            print(f"nextNode is {curr.next.val}")
        curr.next = prev_node # reverse ptr direction
        prev_node = curr # current node will be prev for next iter
        if curr:
            print(f"prevNode is {curr.val}")
        curr = next_node # move curr to next node
        if next_node:
            print(f"new curr is {next_node.val}\n")
    
    print(f"curr: {curr} | prev: {prev_node.val} | next: {next_node}")
    return prev_node

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # ex:
    # A -> B -> C -> D -> E -> F
    # => B -> A -> D -> C -> F -> E
    
    # edge case for 0/1 lists
    if not head or not head.next:
        return head
    
    
    # reference to second node, i.e. what to return
    # i.e. B
    dummy = head.next 
    
    prev = None
    while head and head.next:
        
        # Connect previous pair to rest of list
        # e.g. connecting A -> D
        # reference to D if prev not null (i.e. element next to nextNode when head = nextNode)
        if prev:
            prev.next = head.next
            

        # set prev to head
        prev = head
        
        # Step 2 (save rest of list)
        #reference to remaining list, i.e. C
        next_node = head.next.next 
        
        # Step 1 (edge swap)
        # get second node next to point back to first node
        # e.g. from A->B to A <-> B
        head.next.next = head 
        
        # move head ptr to the remaining list (i.e. A -> C) 
        head.next = next_node
        
        # move head to the head of the remaining list
        head = next_node 
    
    return dummy
def main():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    head = one
    reverse_list(head)
    

if __name__ == "__main__":
    main()

# Example usage:
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3
# reversed_head = reverse_list(node1)