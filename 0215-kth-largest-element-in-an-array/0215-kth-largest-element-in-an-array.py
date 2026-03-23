# 1. 문제 이해
# - [3, 2, 1, 5, 6, 4]
# - k = 2
# - return the kth largest lement in the arry

# 2. 설계
# - min heap
# - if len(heap) > k -> pop
# - return the first value

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
