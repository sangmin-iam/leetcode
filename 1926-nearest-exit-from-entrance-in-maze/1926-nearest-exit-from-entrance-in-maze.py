# 1. 문제 이해
# - 현재 위치에서 exit 찾기
# - exit는 maze의 border -> y = 0, x = 0, y = m - 1 or x = n - 1 and y, x == '+'
# - BFS로 좌우상하 이동

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        current_y, current_x = entrance

        queue = deque([(current_y, current_x, 0)])
        visited = set({(current_y, current_x)})
        
        m = len(maze)
        n = len(maze[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            current_level_nodes = len(queue)

            for _ in range(current_level_nodes):
                y, x, step = queue.popleft()

                for dy, dx in directions:
                    next_y = y + dy
                    next_x = x + dx

                    is_valid = 0 <= next_y < m and 0 <= next_x < n
                    if is_valid:
                        if maze[next_y][next_x] == '.' and (next_y, next_x) not in visited:
                            if next_y == 0 or next_x == 0 or next_y == m - 1 or next_x == n - 1:
                                return step + 1

                            visited.add((next_y, next_x))
                            queue.append((next_y, next_x, step + 1))


        return -1
    