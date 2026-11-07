# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        o = head
        l = ListNode(o.val)
        while o.next is not None:
            o = o.next
            l = self.insertValBack(l, o.val)
        return l
            
    def insertValBack(self, node: ListNode, val):
        return ListNode(val, node)
        