# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)[1]
        

    def height(self, root: Optional[TreeNode]) -> Tuple[int, bool]:
        if root is None: return 0, True
        hl, ball = self.height(root.left)
        hr, balr = self.height(root.right)
        bal = ball and balr and abs(hl-hr) <= 1
        return max(hl, hr) + 1, bal

        