# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        right = []
        left = []
        
        def traverseRight(nodeR):
            if not nodeR:
                right.append(-1)
            else:
                right.append(nodeR.val)
                traverseRight(nodeR.left)
                traverseRight(nodeR.right)

        def traverseLeft(nodeL):
            if not nodeL:
                left.append(-1)
            else:
                left.append(nodeL.val)
                traverseLeft(nodeL.right)
                traverseLeft(nodeL.left)

        traverseRight(root.right)
        traverseLeft(root.left)
        
        return True if right == left else False