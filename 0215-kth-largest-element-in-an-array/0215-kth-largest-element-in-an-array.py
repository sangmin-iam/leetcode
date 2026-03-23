# 1. 문제 이해
# - [3, 2, 1, 5, 6, 4]
# - k = 2
# - return the kth largest lement in the arry

# 2. 설계
# - min heap
# - if len(heap) > k -> pop
# - return the first value

# 3. 복잡도
# TC: O(n log k)
# SC: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums: # O(n)
            heapq.heappush(heap, num) # O(log k)

            if len(heap) > k:
                heapq.heappop(heap) # O(log k)
        
        return heap[0]
