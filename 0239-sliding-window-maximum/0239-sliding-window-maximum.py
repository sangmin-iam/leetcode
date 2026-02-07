class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        # double ended queue 사용 (인덱스 저장)
        queue = collections.deque()

        for i in range(len(nums)):
            # monotonically not-increasing
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            # Add the maximum value
            queue.append(i)

            # Remove the element outside of window
            if queue[0] + k == i:
                queue.popleft()
            
            # Add the result only when the window size is reached
            if i >= k - 1:
                result.append(nums[queue[0]])
    
        return result
