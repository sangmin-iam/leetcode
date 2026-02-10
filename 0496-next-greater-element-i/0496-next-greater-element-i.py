class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # increasing
        nextGreaterMap = {} # Save next greater element from nums2
        
        for n in nums2:
            nextGreaterMap[n] = -1
            
            while stack and stack[-1] < n:
                nextGreaterMap[stack.pop()] = n
            
            stack.append(n)
        
        result = []
        for n in nums1:
            result.append(nextGreaterMap[n])
        
        return result
