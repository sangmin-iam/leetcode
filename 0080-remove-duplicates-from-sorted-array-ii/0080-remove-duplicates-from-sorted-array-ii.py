class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        e = 0

        while e < len(nums):
            count = 1

            while e + 1 < len(nums) and nums[e] == nums[e + 1]:
                count += 1
                e += 1
            
            for i in range(min(2, count)):
                nums[s] = nums[e]
                s += 1
            e += 1

        return s