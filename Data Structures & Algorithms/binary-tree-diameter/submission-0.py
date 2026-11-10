# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.height(root, res)
        return res[0]
    
    def height(self, root: Optional[TreeNode], res) -> int:
        if root is None: 
            return 0
        a = self.height(root.left, res)
        b = self.height(root.right, res)

        if a+b > res[0]:
            res[0] = a+b
        return max(a, b) + 1
    
        