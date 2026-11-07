# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hook = head
        current = head
        after_n = head
        for i in range(n):
            after_n = after_n.next
        
        if after_n is None: 
            return current.next
        while after_n.next:
            after_n = after_n.next
            current = current.next
        current.next = current.next.next
        return hook
        