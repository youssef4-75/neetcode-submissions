# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: return subRoot is None
        return (self.equal(root, subRoot) 
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
    
    def equal(self, tree1, tree2):
        if not tree1 or not tree2:
            return tree1 is tree2
        return (tree1.val == tree2.val
            and self.equal(tree1.left, tree2.left) 
            and self.equal(tree1.right, tree2.right) 
            )