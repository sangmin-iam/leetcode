class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() # (y, x)
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        n = len(grid) # len of y
        m = len(grid[0]) # len of x

        def search(y, x):
            for dy, dx in directions:
                nextY = y + dy
                nextX = x + dx

                if ((nextY, nextX) not in seen) and (0 <= nextY < n and 0 <= nextX < m) and grid[nextY][nextX] == "1":
                    seen.add((nextY, nextX))
                    search(nextY, nextX)


        result = 0

        for y in range(n):
            for x in range(m):
                if (y, x) not in seen and grid[y][x] == "1":
                    result += 1
                    seen.add((y, x))
                    search(y, x)
        
        return result
