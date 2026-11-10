# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.minMaxValid(root)[2]


    def minMaxValid(self, root):
        if root is None: 
            return None, None, True
        minl, maxl, validl = self.minMaxValid(root.left)
        minr, maxr, validr = self.minMaxValid(root.right)
        if maxl is None:
            maxl = root.val - 1
            minl = root.val
        if minr is None:
            minr = root.val + 1
            maxr = root.val 
        valid = (maxl < root.val < minr) and validl and validr
            
            
        return minl, maxr, valid

        
        