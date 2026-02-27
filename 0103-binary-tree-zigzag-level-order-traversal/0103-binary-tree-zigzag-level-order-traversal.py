# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        left_to_right = True
        
        queue = deque([root])
        result = []
        
        while queue:
            current_level_nodes = len(queue)
            temp = deque()
                
            for _ in range(current_level_nodes):
                node = queue.popleft()
                
                if left_to_right:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(list(temp))
            left_to_right = not left_to_right
        
        return result
            