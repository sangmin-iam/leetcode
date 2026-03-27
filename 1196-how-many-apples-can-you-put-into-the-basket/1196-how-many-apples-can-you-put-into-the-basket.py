class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # O(n log n)
        weight.sort()

        result = 0
        remaining = 5000
        for w in weight: # O(n)
            if w <= remaining:
                remaining -= w
                result += 1
            else:
                break
        
        return result
            