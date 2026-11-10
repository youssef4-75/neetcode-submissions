# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None: return res
        file = [[root, 0]]
        

        while file:
            tree, level = file.pop(0)
            
            if tree.left: file.append([tree.left, level+1])
            if tree.right: file.append([tree.right, level+1])
          

            if len(res) < level+1:
                res.append([])
            res[level].append(tree.val)
        return res
        

        