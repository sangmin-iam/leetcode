class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 1. k가 nums의 길이와 같으면 1바퀴를 돌은 것과 동일
        k = k % len(nums) 

        # 2. Reverse (Whole)
        l = 0
        r = len(nums) - 1
        while l < r:
            # Swap
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # 3. Reverse (Left - First K Elements)
        l = 0
        r = k - 1
        while l < r:
            # Swap
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # 4. Reverse (Right - After K Elements)
        l = k
        r = len(nums) - 1
        while l < r:
            # Swap
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        