# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        range_sum = 0
        if low <= root.val <= high:
            range_sum += root.val
        if low < root.val:
            range_sum += self.rangeSumBST(root.left, low, high)
        if high > root.val:
            range_sum += self.rangeSumBST(root.right, low, high)
        
        return range_sum