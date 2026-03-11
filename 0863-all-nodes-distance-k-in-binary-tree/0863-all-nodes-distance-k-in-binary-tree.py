# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. 문제 이해
# K distance from target node
# 2. 문제 설계 
# Tree -> Graph
# Traverse tree -> Link each node to its parent
# Travese the graph from K

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)

        # Traverse the graph from K (BFS)

        queue = deque([target])
        visited = set({target})

        distance = 0

        while queue and distance < k:
            current_level_len = len(queue)

            for _ in range(current_level_len):
                node = queue.popleft()

                for next_node in [node.left, node.right, node.parent]:
                    if next_node and next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)
            
            distance += 1
        
        result = []

        for node in queue:
            result.append(node.val)
    
        return result
