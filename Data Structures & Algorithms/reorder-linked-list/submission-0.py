# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        n = 0
        hook = head 
        while head:
            n+= 1
            head = head.next
        head = hook
        rev = self.reverseList(head)
        print(rev.val, head.val)
        pair = n%2 == 1
        n = n//2
        while head and head.next and n>0:
            print(rev.val, head.val)
            hook = rev.next
            rev.next = head.next
            if pair or n!=1: head.next = rev
            head = rev.next
            rev = hook
            n -= 1
        head.next = None
        


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        o = head
        l = ListNode(o.val)
        while o.next is not None:
            o = o.next
            l = ListNode(o.val, l)
        return l

        
        



