class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # Create minimum heap
        heapq.heapify(sticks) # O(n)

        cost = 0
        while len(sticks) > 1:
            x = heapq.heappop(sticks) # O(log n)
            y = heapq.heappop(sticks) # O(log n)

            cost += x + y

            heapq.heappush(sticks, x + y) # O(log n)
        
        return cost
