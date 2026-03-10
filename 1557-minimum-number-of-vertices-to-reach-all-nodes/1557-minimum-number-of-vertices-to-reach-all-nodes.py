class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n

        for _, b in edges:
            indegrees[b] += 1
        
        result = []

        for i in range(n):
            if indegrees[i] == 0:
                result.append(i)
        
        return result
