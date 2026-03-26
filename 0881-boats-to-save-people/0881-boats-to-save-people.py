# TC: O(n log n)
# SC: O(1) or O(n)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # O(n log n)

        l = 0
        r = len(people) - 1
        count = 0

        while l <= r: # O(n)
            if people[l] + people[r] <= limit:
                l += 1
            
            r -= 1
            count += 1
        
        return count
    