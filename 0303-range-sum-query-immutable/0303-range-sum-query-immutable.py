class NumArray:
    def __init__(self, nums: List[int]):
        if not nums:
            self.acc = []
            return
        
        self.acc = [nums[0]]
        for i in range(1, len(nums)):
            self.acc.append(self.acc[i - 1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        sumLeft = self.acc[left - 1] if left > 0 else 0
        sumRight = self.acc[right]
    
        return sumRight - sumLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)