class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(y, x):
            visited.add((y, x))

            area = 1

            for dy, dx in directions:
                next_y = y + dy
                next_x = x + dx

                if (next_y, next_x) not in visited:
                    if (0 <= next_y < len(grid)) and (0 <= next_x < len(grid[0])) and (grid[next_y][next_x] == 1):
                        area += dfs(next_y, next_x)
            
            return area
            
        max_count = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) not in visited:
                    if grid[y][x] == 1:
                        max_count = max(dfs(y, x), max_count)
            
        return max_count
