class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        res = 0

        # get middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd part of the list
        curr, prev = slow, None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # get max sum of pairs
        while prev:
            res = max(res, head.val + prev.val)
            prev = prev.next
            head = head.next

        return res