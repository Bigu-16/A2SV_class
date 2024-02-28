# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode_dict = defaultdict(int)
        ans = []

        def mode(node):
            if node:
                mode_dict[node.val] += 1
                mode(node.left)
                mode(node.right)
        
        mode(root)
        max_ = max(mode_dict.values())

        for key,val in mode_dict.items():
            if val == max_:
                ans.append(key)

        return ans