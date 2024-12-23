class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")
        cursum = 0
        start = 0
        
        for end in range(len(nums)):
            cursum += nums[end]
            
            while cursum >= target:
                minLength = min(minLength, end - start + 1)
                cursum -= nums[start]
                start += 1
        
        return 0 if minLength == float("inf") else minLength