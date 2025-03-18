# Boyer-Moore Voting Algorithm
# TC - O(N)
# SC - O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curNum = 0

        for n in nums:
            if count == 0:
                curNum = n
            
            if curNum == n:
                count += 1
            else:
                count -= 1
        
        return curNum

