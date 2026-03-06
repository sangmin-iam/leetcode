# TC: O(n)
# SC: O(n)

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 1. Graph (Undirected)
        graph = defaultdict(list)
        # 2. Roads (Original)
        roads = set()
        
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))
        
        seen = set()
        seen.add(0)

        def dfs(node):
            count = 0

            for next_node in graph[node]:
                if next_node not in seen:
                    if (node, next_node) in roads:
                        count += 1
                    seen.add(next_node)
                    count += dfs(next_node)

            return count

        return dfs(0)
        