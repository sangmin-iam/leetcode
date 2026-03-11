class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        queue = deque([(0, 0, 1)]) # y, x, step
        visited = set({0, 0})

        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]
        
        n = len(grid)

        while queue:
            y, x, step = queue.popleft()
            
            if y == n - 1 and x == n - 1:
                return step
            
            for dy, dx in directions:
                next_y = y + dy
                next_x = x + dx

                if 0 <= next_y < n and 0 <= next_x < n and (next_y, next_x) not in visited and grid[next_y][next_x] == 0:
                    visited.add((next_y, next_x))
                    queue.append((next_y, next_x, step + 1))

        return -1