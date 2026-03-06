class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        n = len(isConnected)
        for y in range(n):
            for x in range(y + 1, n):
                if isConnected[y][x] == 1:
                    graph[y].append(x)
                    graph[x].append(y)
        
        seen = set()

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        provinces = 0

        for i in range(n):
            if i not in seen:
                provinces += 1
                seen.add(i)
                dfs(i)
        
        return provinces