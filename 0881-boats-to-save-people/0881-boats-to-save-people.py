# TC: O(n log n)
# SC: O(1)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Limit: Maximum 3
        # People: Weight [3, 2, 2, 1]
        # 사람들의 Weight는 항상 Limit보다 작거나 같음
        # 1. 정렬 [1, 2, 2, 3]
        people.sort()
    
        # 2. Two Pointer
        l = 0
        r = len(people) - 1
        count = 0
        
        while l <= r:
            remaining = limit - people[r]
            r -= 1
            count += 1

            if remaining >= people[l] and l <= r:
                l += 1
        
        return count
