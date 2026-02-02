class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 1. Initialize variables
        left = 0
        flippedCount = 0
        result = 0
        
        # 2. For Loop
        for right in range(0, len(nums)):
            if nums[right] == 0:
                flippedCount += 1
            
            while flippedCount > k:
                # Subtract first
                if nums[left] == 0:
                    flippedCount -= 1
                
                # then move to the right
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
