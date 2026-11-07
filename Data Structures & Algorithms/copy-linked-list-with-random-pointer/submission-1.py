"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        
        deep_copy = Node(head.val)
        already_copied = {}
        hook = head
        hook_copy = deep_copy
        n = 0
        while head:
            deep_copy.val = head.val
            deep_copy.next = None if head.next is None else Node(head.next.val)
            already_copied[head] = deep_copy

            


            deep_copy = deep_copy.next
            head = head.next
        deep_copy = hook_copy
        head = hook

        while head:
            deep_copy.random = already_copied.get(head.random, None)
            deep_copy = deep_copy.next
            head = head.next
        return hook_copy

