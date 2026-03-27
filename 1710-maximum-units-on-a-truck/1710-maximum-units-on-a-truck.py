# 문제 이해
# [1, 3] -> boxes, units
# Unit이 가장 높은거만 먼저 사용

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # MaxHeap (with units)
        maxHeap = []
        for boxType in boxTypes:
            boxes, units = boxType

            heapq.heappush(maxHeap, (-units, boxes))
        
        result = 0
        while maxHeap and truckSize > 0:
            units, boxes = heapq.heappop(maxHeap)
            
            if boxes <= truckSize:
                result += (-units) * boxes
                truckSize -= boxes
            else:
                result += truckSize * (-units)
                truckSize -= boxes
        
        return result
