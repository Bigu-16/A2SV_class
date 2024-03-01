# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = 0
        node_dict = defaultdict(list)
        
        def traverse(node):
            nonlocal count
            if not node:
                return
            
            if count % 2 == 0:
                node_dict[count].append(node.val)
            else:
                node_dict[count] = [node.val] + node_dict[count]
            
            count += 1
            left = traverse(node.left)
            right = traverse(node.right)
            count -= 1

        traverse(root)
        return node_dict.values()
