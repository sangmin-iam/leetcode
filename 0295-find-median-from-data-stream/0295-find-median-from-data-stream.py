# 1. Max Heap / Min Heap (Sorted in order) - Max Heap에 Median값을 담을 예정
# 2. addNum Algorithm
# - Add num to Max Heap
# - Pop num from Max Heap
# - Add the num to Min Heap
# - if Min Heap > Max Heap - Pop from min heap and move it to max heap

# 3. findMedian
# - len(max_heap) == len(max_heap) -> max_heap[0] + min_heap[0] / 2
# - else -> max_heap[0]

# TC: O(log n) -> heap operations
# SC: O(n) -> Store heaps
class MedianFinder:
    def __init__(self):
        self.max_heap = [] # find median here
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()