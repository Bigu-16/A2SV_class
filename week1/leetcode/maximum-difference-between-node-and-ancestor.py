# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def traverse(node, max_val, min_val):
            nonlocal max_diff
            
            if not node:
                return
            
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            
            max_diff = max(max_diff, max_val - min_val)
            
            traverse(node.left, max_val, min_val)
            traverse(node.right, max_val, min_val)
        
        traverse(root, root.val, root.val)
        
        return max_diff


