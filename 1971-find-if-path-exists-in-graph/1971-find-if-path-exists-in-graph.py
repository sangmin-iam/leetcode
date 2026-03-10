class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        
        def search(node):
            if node == destination:
                return True

            neighbors = adj[node]

            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                
                visited.add(neighbor)
                if search(neighbor):
                    return True
            
            return False
        
        visited.add(source)
        return search(source)