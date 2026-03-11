# 1. 문제 이해
# - 노드 0에서 부터 이동해서 restricted를 제외하고 어느 몇 개의 노드를 갈 수 있는가?

# 2. 설계
# - restricted -> set
# - edges -> Adjacent List로 변경
# - 0부터 neighbor를 방문하면서 restricted가 존재하면 그 자리에서 리턴

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restrictedNodes = set(restricted)

        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node: int) -> int:
            if node in restrictedNodes:
                return 0
            
            visited.add(node)

            count = 1

            for neighbor in adj[node]:
                if neighbor not in visited:
                    count += dfs(neighbor)
            
            return count

        return dfs(0)