class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)

        n = len(bombs)
        for i in range(n): # [0, ...]
            for j in range(i + 1, n): # [1, ...]
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                
                if distance_squared <= r1 ** 2:
                    adj[i].append(j)

                if distance_squared <= r2 ** 2:
                    adj[j].append(i)

        maxCount = 0
        for i in range(n):
            queue = deque()
            queue.append(i)
            visited = set({i})

            while queue:
                node = queue.popleft()

                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            
            maxCount = max(maxCount, len(visited))

        return maxCount