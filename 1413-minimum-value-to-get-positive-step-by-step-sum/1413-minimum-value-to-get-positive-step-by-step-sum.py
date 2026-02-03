class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_total = 0
        total = 0

        for i in range(len(nums)):
            total += nums[i]    
            min_total = min(min_total, total)
        
        return 1 if min_total >= 0 else -min_total + 1
