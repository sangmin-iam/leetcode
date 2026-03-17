# 1. 문제 이해
# - i에서 i + arr[i] 혹은 i - arr[i] 가능 (그래프라고 생각하기)
# - value가 0인 인덱스를 도달할 수 있는지 체크

# 2. 문제 설계
# - 그래프 만들기 (adj 활용)

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        adj = defaultdict(list)

        n = len(arr)
        for i in range(n):
            left = i - arr[i]
            right = i + arr[i]

            if left >= 0:
                adj[i].append(left)

            if right < n:
                adj[i].append(right)
        
        queue = deque()
        queue.append(start)
        visited = set({start})

        while queue:
            current_node = queue.popleft()

            for neighbor in adj[current_node]:
                if neighbor == current_node:
                    return True
                
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False
