# TC: O(log n)
# SC: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        minNum = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])
                break

            mid = (l + r) // 2
            minNum = min(minNum, nums[mid])

            isSorted = nums[mid] >= nums[l]
            if isSorted:
                l = mid + 1
            else:
                r = mid - 1
        
        return minNum