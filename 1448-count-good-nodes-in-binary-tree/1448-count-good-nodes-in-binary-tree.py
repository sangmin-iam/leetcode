# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 문제 이해
# - Find Good Node
# - Good Node: No nodes with a value greater than current node (current should be the greatest num in the path)
# 2. 문제 설계
# - Traverse (dfs)
# - maximumVal, node
# - int
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximumVal):
            if not node:
                return 0

            left = dfs(node.left, max(maximumVal, node.val))
            right = dfs(node.right, max(maximumVal, node.val))
            
            count = left + right

            if node.val >= maximumVal:
                count += 1
            
            return count
        
        return dfs(root, float('-inf'))
