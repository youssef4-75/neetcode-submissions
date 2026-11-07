# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        node1 = list1
        node2 = list2

        result = ListNode()
        head = result

        while node1 is not None and node2 is not None:
            result.next = ListNode()
            result = result.next
            if node1.val < node2.val:
                result.val = node1.val
                node1 = node1.next
            else:
                result.val = node2.val
                node2 = node2.next
            
        result.next = node2 if node1 is None else node1
        return head.next
        

        