class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = defaultdict(int)
        
        for ch in magazine:
            counts[ch] += 1
        
        for ch in ransomNote:
            if counts[ch] > 0:
                counts[ch] -= 1
            else:
                return False
        
        return True