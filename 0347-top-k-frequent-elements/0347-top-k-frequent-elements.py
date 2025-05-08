# TC: O(n)
# SC: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        # 1. HashMap Count
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        # 2. frequency
        frequency = [[] for _ in range(len(nums) + 1)]

        # 3. [] - index -> count, value -> num
        for n, cnt in count.items():
            frequency[cnt].append(n)
        
        # 4. 뒤에서 앞으로 오면서 하나씩 확인하고 있으면 k를 1씩 줄이고, result 배열에 담기
        for i in range(len(nums), 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result
        
        return result