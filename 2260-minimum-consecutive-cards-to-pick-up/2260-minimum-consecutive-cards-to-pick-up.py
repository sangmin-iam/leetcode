# TC: O(n)
# SC: O(n)
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        matching = defaultdict(list)
        
        # iterate over cards
        for i, card in enumerate(cards):
            matching[card].append(i)
        
        # iterate over matching hashMaps
        # and find the closest two cards - the closest distance
        result = math.inf
        for i in matching:
            for idx in range(len(matching[i]) - 1):
                result = min(result, matching[i][idx + 1] - matching[i][idx] + 1)
        
        return result if result < math.inf else -1