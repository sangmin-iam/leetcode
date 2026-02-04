class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # 1. Get prefix sum
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        # 2. Get Result
        result = []
        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                result.append(-1)
            else:
                subArraySum = prefix[i + k] - prefix[i - k] + nums[i - k]
                subArrayAverage = subArraySum // (1 + (k * 2))
                
                result.append(subArrayAverage)
        
        return result
            