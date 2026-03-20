# 1. 목표 Sum
# 2. 초기 Sum
# 3. max_heap으로 변경
# 4. 꺼내면 초기에서 (-)하고 다시 반으로 나누어서 (+)
# TC: O(n log n)
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        initSum = sum(nums)
        targetSum = initSum / 2

        nums = [-num for num in nums]
        heapq.heapify(nums)
        curSum = initSum
        count = 0

        print(curSum)
        print(targetSum)

        while nums:
            if curSum <= targetSum:
                return count

            num = abs(heapq.heappop(nums))
            curSum -= num
            curSum += num / 2
            heapq.heappush(nums, -(num / 2))
            count += 1

        return count

