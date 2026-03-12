# 1. 문제 이해
# - 좌상단 -> 우하단 몇 번만의 도달 가능한지 구하기
# - k 만큼 obstacles 지울 수 있음 (remaining)

# 2. 문제 설계
# BFS -> queue y, x, remaining, steps으로 트래킹
# visited -> (y, x, reamaing)
# 우하단에 도달하면 steps 리턴

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0, 0, k, 0)])
        visited = set({(0, 0, k)})
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        m = len(grid)
        n = len(grid[0])

        while queue:
            current_lev_nodes = len(queue)

            for _ in range(current_lev_nodes):
                y, x, remaining, steps = queue.popleft()

                if y == m - 1 and x == n - 1:
                    return steps
                
                for dy, dx in directions:
                    next_y = y + dy
                    next_x = x + dx

                    isValid = 0 <= next_y < m and 0 <= next_x < n
                    if isValid:
                        # No obstacle
                        if grid[next_y][next_x] == 0 and (next_y, next_x, remaining) not in visited:
                            visited.add((next_y, next_x, remaining))
                            queue.append((next_y, next_x, remaining, steps + 1))
                        # Obstacle + Remaining exists
                        elif remaining and (next_y, next_x, remaining - 1) not in visited:
                            visited.add((next_y, next_x, remaining - 1))
                            queue.append((next_y, next_x, remaining - 1, steps + 1))
            
        return -1
