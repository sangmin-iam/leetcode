# TC: O(n log k)
# SC: O(k)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        def getDistance(x, y):
            return math.sqrt(x ** 2 + y ** 2)
        
        for x, y in points: # O(n)
            distance = getDistance(x, y)
            heapq.heappush(maxHeap, (-distance, x, y)) # O(log k)

            if len(maxHeap) > k:
                heapq.heappop(maxHeap) # O(log k)
        
        result = []
        
        for _, x, y in maxHeap:
            result.append([x, y])
        
        return result
            