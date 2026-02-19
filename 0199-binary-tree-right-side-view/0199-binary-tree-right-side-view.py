# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            nodes_in_current_level = len(queue)

            right_side_node = queue[-1]
            result.append(right_side_node.val)
            
            for _ in range(nodes_in_current_level):
                current_node = queue.popleft()

                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
        
        return result
