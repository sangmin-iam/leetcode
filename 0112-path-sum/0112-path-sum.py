# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            if not node:
                return False

            if not node.left and not node.right:
                if targetSum == currentSum + node.val:
                    return True

            leftSum = dfs(node.left, currentSum + node.val)
            rightSum = dfs(node.right, currentSum + node.val)

            return leftSum or rightSum

        
        result = dfs(root, 0)

        return result