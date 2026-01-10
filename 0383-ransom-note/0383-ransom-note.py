# 1. Understand Problem
# Inputs
# - randsomeNote
# - magazine
# Output
# - Does magazine have all the letters from ransomeNote? -> if one is missing then is done

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count -> HashMap
        ransomNoteCnt = defaultdict(int)
        magazineCnt = defaultdict(int)
        
        # Count letters
        for ch in ransomNote:
            ransomNoteCnt[ch] += 1
        for ch in magazine:
            magazineCnt[ch] += 1
        
        # Iterate ransomeNote and compare the number of letters
        for key in ransomNoteCnt:
            a = ransomNoteCnt[key]
            b = magazineCnt[key]
            
            if a <= b and a > 0:
                continue
            
            if a != b:
                return False
        
        return True