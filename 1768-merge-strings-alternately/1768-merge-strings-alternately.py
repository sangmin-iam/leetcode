"""
:type word1: str
:type word2: str
:rtype: str
"""

# TC: O(N + M)
# SC: O(N + M)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        
        l = 0
        r = 0

        while l < len(word1) and r < len(word2):
            result.append(word1[l])
            result.append(word2[r])

            l += 1
            r += 1
        
        while l < len(word1):
            result.append(word1[l])
            l += 1
        
        while r < len(word2):
            result.append(word2[r])
            r += 1
        
        return "".join(result)


        