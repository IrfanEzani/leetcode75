#!/usr/bin/env python3

from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next
    
# use dummy pointer
def get_sum(head):
    ans = 0
    dummy = head
    while dummy:
        ans += dummy.val
        dummy = dummy.next
    
    # same as before, but we still have a pointer at the head
    return ans
    
def get_middle(head):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

# 141
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

# set solution for 141
def hasCycle(self, head: Optional[ListNode]) -> bool:
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

def main():
    one = ListNode(1)
    two = ListNode(1)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    six = ListNode(6)
    
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six 
    head = one
    
    while head and head.next:
        print(f"{head.val}")
        if head.val == head.next.val:
            head.next = head.next.next
        head = head.next
    
    
    return 0
    
if __name__ == "__main__":
    main()