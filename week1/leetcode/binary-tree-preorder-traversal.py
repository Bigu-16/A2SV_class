# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def Traverse(new_val):
            if new_val:
                ans.append(new_val.val)

                Traverse(new_val.left)
                Traverse(new_val.right)

        Traverse(root)
        return ans
            