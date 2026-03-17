# 1. 문제 이해
# - startGene -> endGene
# - One mutation -> One Single character change ['A', 'C', 'G', 'T']
# - Bank: Valid genes (바꿨을때 여기 없으면 포함 안시킴)

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        queue.append((startGene, 0))
        visited = set({startGene})

        while queue:
            gene, level = queue.popleft()

            if gene == endGene:
                return level

            for i in range(len(gene)):
                for ch in 'ACGT':
                    next_gene = gene[:i] + ch + gene[i + 1:]

                    if next_gene in bank and next_gene not in visited:
                        queue.append((next_gene, level + 1))
                        visited.add(next_gene)
        
        return -1
