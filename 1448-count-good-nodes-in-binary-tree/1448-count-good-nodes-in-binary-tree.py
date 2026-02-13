# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iteratively
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]

        result = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                result += 1
            
            if node.left:
                stack.append((node.left, max(node.val, max_val)))
            if node.right:
                stack.append((node.right, max(node.val, max_val)))
            
        return result
