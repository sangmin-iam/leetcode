class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Create a graph (*it, h*t, *ot) - Singlet letter difference
        nei = defaultdict(list) # { *it: [hit], h*t: [hit, hot] }
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        # BFS
        queue = deque([beginWord])
        visited = set({beginWord})
        
        result = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                
                if word == endWord:
                    return result
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            queue.append(neiWord)
                            visited.add(neiWord)
            
            result += 1
        
        return 0
