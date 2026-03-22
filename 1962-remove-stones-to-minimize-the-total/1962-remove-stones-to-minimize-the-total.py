# 1. 문제 이해
# - Select piles[i]
# - Remove floor(piles[i] / 2) stones from it
# - Return the minimum possible total number of stones remaining after apply the k operations

# 2. 문제 설계
# - Get current sum
# - Pick the biggest (create max heap)
# - Operate
# - Save, subtract

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-stone for stone in piles]
        heapq.heapify(maxHeap)

        for _ in range(k):
            stone = abs(heapq.heappop(maxHeap))
            nextStone = stone - math.floor(stone / 2)
            heapq.heappush(maxHeap, -nextStone)

        return -sum(maxHeap)
        