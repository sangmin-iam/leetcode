# TC: O(n log k)
# SC: O(n + k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Hashmap Count (num: count)
        counts = Counter(nums)
        
        # 2. Get top k elements using min heap
        heap = [] # min heap (count, num)
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = [pair[1] for pair in heap]
        
        return result

        