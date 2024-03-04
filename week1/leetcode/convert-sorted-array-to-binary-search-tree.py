# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def traverse(left,right):
            if left > right:
                return

            mid = (left + right) // 2
            left = traverse(left,mid-1)
            right = traverse(mid+1,right)

            return TreeNode(nums[mid],left,right)

        return traverse(0,len(nums)-1) 