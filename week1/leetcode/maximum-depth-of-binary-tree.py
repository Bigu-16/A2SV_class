# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count_r = 0
        count_l = 0

        def traverse(node):
            if not node:
                return 0
            else:
                count_r = 1 + traverse(node.right)
                count_l = 1 + traverse(node.left)
            return max(count_r,count_l)
        return traverse(root)