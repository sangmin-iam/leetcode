# 1. 문제 이해
# - i에서 i + arr[i] 혹은 i - arr[i] 가능 (그래프라고 생각하기)
# - value가 0인 인덱스를 도달할 수 있는지 체크

# 2. 문제 설계
# - 그래프 만들기 (adj 활용)

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        queue.append(start)
        visited = set({start})

        while queue:
            node = queue.popleft()

            if arr[node] == 0:
                return True

            for neighbor in [node - arr[node], node + arr[node]]:
                if neighbor not in visited and 0 <= neighbor < len(arr):
                    if arr[neighbor] == 0:
                        return True

                    queue.append(neighbor)
                    visited.add(neighbor)

        return False
