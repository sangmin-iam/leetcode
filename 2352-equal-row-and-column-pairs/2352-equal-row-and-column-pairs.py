class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # 1. iterate over and save cols and rows with count
        rows = defaultdict(int)
        cols = defaultdict(int)

        # rows
        for i in range(len(grid)):
            row = tuple(grid[i])
            rows[row] += 1
        
        # cols
        for x in range(len(grid[0])):
            current_col = []
            
            for y in range(len(grid[x])):
                num = grid[y][x]
                current_col.append(num)
            
            cols[tuple(current_col)] += 1
        
        # 2. Calculate Matching Count
        result = 0
        for r in rows:
            result += cols[r] * rows[r]
        
        return result