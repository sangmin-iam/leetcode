# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        return self.dfs(root, 1)

    def dfs(self, node: Optional[TreeNode], level: int) -> int:
        if not node:
            return level - 1
        
        left = self.dfs(node.left, level + 1)
        right = self.dfs(node.right, level + 1)

        return max(left, right)
    
