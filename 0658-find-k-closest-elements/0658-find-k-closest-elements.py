# TC: O((n + k) * log k)
# SC: O(k)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Using max heap (distance, element)
        heap = []

        for num in arr: # O(n)
            distance = abs(x - num)
            heapq.heappush(heap, (-distance, -num)) # O(log k)

            if len(heap) > k:
                heapq.heappop(heap) # O(log k)
        
        result = sorted([-pair[1] for pair in heap]) # O(k log k)

        return result
