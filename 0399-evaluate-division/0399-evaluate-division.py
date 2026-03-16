# 1. 문제 이해
# equations = [[a, b], [b, c]]
# values = [2, 3]
# [queries] = [[a, c], [c, a]]
# 2 * 3 = 6, 1/2 * 1/3 = 1/6

# 2. 문제 해결
# adj
# bfs for each query

# TC: O(N * E)
# SC: O(V + E)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, equa in enumerate(equations): # index, [a, b]
            a, b = equa
            
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]]) # Reverse
        
        result = []

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            queue = deque()
            visited = set()

            queue.append((src, 1)) # node, weight
            visited.add(src)

            while queue:
                node, weight = queue.popleft()

                if node == target:
                    return weight

                for neighbor, neighbor_weight in adj[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, weight * neighbor_weight))
                        visited.add(neighbor)
            
            return -1
    
        for q in queries:
            src, target = q

            result.append(bfs(src, target))
        
        return result
