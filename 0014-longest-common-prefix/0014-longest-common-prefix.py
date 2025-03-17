class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        res = 0
        for x in range(len(prefix)):
            for y in range(len(strs)):
                if x == len(strs[y]): # 범위 벗어나는 경우
                    return prefix[:res]
                if prefix[x] != strs[y][x]: # 다른 경우
                    return prefix[:res]
            res += 1
    
        return prefix[:res]
            