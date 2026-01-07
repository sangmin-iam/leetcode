class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sortedStr = "".join(sorted(s))
            groups[sortedStr].append(s)
        
        return list(groups.values())