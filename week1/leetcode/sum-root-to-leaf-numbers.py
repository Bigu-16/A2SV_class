# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, summ):
            if not node:
                return 0
            
            summ = summ * 10 + node.val
            if not node.left and not node.right:
                return summ
            
            return traverse(node.left, summ) + traverse(node.right, summ)
            
        return traverse(root, 0)