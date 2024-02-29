# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node1,node2):
            newNode = TreeNode()
            if not node1 and not node2:
                return 
            if node1 and node2:
                newNode.val = node1.val + node2.val
                newNode.right = traverse(node1.right,node2.right)
                newNode.left = traverse(node1.left,node2.left)
                return newNode
            else:
                if node1 and not node2:
                    newNode = node1
                elif node2 and not node1:
                    newNode = node2
                return newNode
                
        return traverse(root1,root2)