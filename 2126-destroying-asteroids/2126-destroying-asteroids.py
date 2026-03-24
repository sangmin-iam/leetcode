# TC: O(n log n)
# SC: O(1)

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        currentMass = mass
        asteroids.sort()

        for asteroid in asteroids:
            if currentMass < asteroid:
                return False
            
            currentMass += asteroid
        
        return True
