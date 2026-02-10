class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque() # Minimum value
        decreasing = deque() # Maximum value

        left = 0
        result = 0

        for right in range(len(nums)):
            # Maintain Monotonic for new number
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            increasing.append(nums[right])
            decreasing.append(nums[right])

            # Max - Min > Limit
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
