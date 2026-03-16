# 1. 문제 이해
# - "0000" 에서 시작
# - target 찾기
# - deadends로는 접근 불가

# 2. 문제 설계
# - deadends에 0000이 있으면 찾을 수 없음 -> -1 리턴
# - 이미 방문한 곳은 가지 않도록 막기
# - BFS로 해결 (shortest path)

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        queue = deque()
        queue.append(("0000", 0)) # [lock, turns]
        visited = set(deadends)

        def children(lock):
            result = []

            for i in range(4):
                # 브랜치 2개 up, down
                next_up_num = (int(lock[i]) + 1) % 10
                next_up_lock = lock[:i] + str(next_up_num) + lock[i + 1:]
                
                next_down_num = (int(lock[i]) - 1 + 10) % 10
                next_down_lock = lock[:i] + str(next_down_num) + lock[i + 1:]

                result.append(next_up_lock)
                result.append(next_down_lock)

            return result

        
        while queue:
            lock, turns = queue.popleft()

            # Found
            if lock == target:
                return turns
            
            for child in children(lock): # ["0001", "0009", "0010", ...]
                print(child)
                if child not in visited:
                    queue.append((child, turns + 1))
                    visited.add(child)
        
        return -1
