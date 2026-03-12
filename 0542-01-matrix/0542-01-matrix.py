# 1. 문제이해
# - Mat에서 0에서 부터 떨어진 거리 구하기 (BFS)
# - Queue 생성
# - Directions 생성
# - Visited 생성
# - queue에 0인 경우 삽입 -> 위치와 함께


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        # queue
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x] == 0:
                    queue.append((y, x, 0)) # y, x, distance
                    visited.add((y, x))

        
        while queue:
            current_level_node = len(queue)

            for _ in range(current_level_node):
                y, x, distance = queue.popleft()

                mat[y][x] = distance

                for dy, dx in directions:
                    next_y = y + dy
                    next_x = x + dx
                    next_distance = distance + 1

                    isNextValid = 0 <= next_y < len(mat) and 0 <= next_x < len(mat[0]) and (next_y, next_x) not in visited
                    if isNextValid:
                        queue.append((next_y, next_x, next_distance))
                        visited.add((next_y, next_x))

        return mat