# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if (p == right and q == left) or (q == right and p == left):
            return root
        if root == p and (q == left or q == right):
            return root
        elif root == q and (p == left or p == right):
            return root

        return left or right


                

                