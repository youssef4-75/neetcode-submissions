# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        res_set = set()
        res_set.add(0)
        res = [root.val]

        file = [(root, 0)]
        
        while file:
            tree, level = file.pop(0)
            val = None
            if tree.right: 
                file.append([tree.right, level+1])
                val = tree.right.val
            if tree.left:
                file.append([tree.left, level+1])
                val = tree.left.val if val is None else val
            if val is None: continue
            if level+1 not in res_set:
                res_set.add(level+1)
                res.append(val)
        return res


        