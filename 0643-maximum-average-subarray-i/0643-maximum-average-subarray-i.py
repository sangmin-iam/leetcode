# Nums, K length

# 1. Fixed Sliding Window 활용
# 2. K length로 초기 윈도우 만들기
# 3. K 부터 가면서 앞에껀 빼고 뒤에는 더해서 새로 계산
# 4. Max Average를 계속 비교하여 저장

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0

        for i in range(0, k):
            curr += nums[i]
        
        result = 0
        result = curr
    
        for i in range(k, len(nums)):
            curr -= nums[i - k]
            curr += nums[i]
            
            result = max(result, curr)
        
        return result / k
        