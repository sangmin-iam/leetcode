# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        values = []
        
        def dfs(node):
            # Base Case
            if not node:
                return
            
            # in-order recursion
            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)
        
        dfs(root)

        result = float("inf")
        
        for i in range(1, len(values)):
            result = min(result, abs(values[i] - values[i - 1]))
    
        return result

