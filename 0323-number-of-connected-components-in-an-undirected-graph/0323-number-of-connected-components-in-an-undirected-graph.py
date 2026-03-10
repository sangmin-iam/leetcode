class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. Adjacent List
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        count = 0

        def dfs(node):
            visited.add(node)

            neighbors = adj[node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        
        return count
