# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_val = root.val
    
        while root:
            is_smaller = abs(root.val - target) < abs(min_val - target)
            is_tie_break = (abs(root.val - target) == abs(min_val - target) and root.val < min_val)

            if abs(root.val - target) < abs(min_val - target) or is_tie_break:
                min_val = root.val
                
            if root.val < target:
                root = root.right
            else:
                root = root.left
    
        return min_val
            