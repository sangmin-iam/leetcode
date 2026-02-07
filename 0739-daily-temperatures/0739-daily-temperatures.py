# TC: O(n)
# SC: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [ ] -> Should be descending
        result = [0] * len(temperatures) 

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        
        return result
