# 1. 문제 이해
# - startGene -> endGene
# - One mutation -> One Single character change ['A', 'C', 'G', 'T']
# - Bank: Valid genes (바꿨을때 여기 없으면 포함 안시킴)

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set(startGene)

        queue = deque()
        queue.append((startGene, 0)) # gene, level

        while queue:
            gene, level = queue.popleft()

            if gene == endGene:
                return level

            for i in range(len(gene)):
                for ch in 'ACGT':
                    new_gene = gene[:i] + ch + gene[i + 1:]
                    if new_gene not in visited and new_gene in bank:
                        queue.append((new_gene, level + 1))
                        visited.add(new_gene)
        
        return -1
