# 1. 문제이해
# profits = [1, 2, 3]
# capital = [0, 1, 1]
# k = 2 (가능한 프로젝트)
# w = 0 (초기 자금)

# 2. 문제 설계
# - capital과 profits을 묶기
# - k번 선택 가능
# - 현재 자금에서 가능한 프로젝트의 profit을 maxheap에 저장
# - 가장 높은 수익이 되는 것을 한 번씩 선택

# TC: O(n log n)
# SC: O(n)

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits)) # O(n log n)
        capital = w
        maxHeap = []
        i = 0
        n = len(profits)
        
        # 프로젝트 수
        for _ in range(k): # O(k)
            # 현재 자금에서 가능한 프로젝트의 profit을 저장
            while i < n and projects[i][0] <= capital: # O(n)
                heapq.heappush(maxHeap, -projects[i][1]) # O(log n)
                i += 1
            
            # 자금이 부족하여 더이상 프로젝트 불가
            if len(maxHeap) == 0:
                return capital

            # 가장 높은 수익을 맡음
            capital += abs(heapq.heappop(maxHeap)) # O(log n)
        
        return capital