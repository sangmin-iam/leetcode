class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1. count
        count = defaultdict(int)

        # 2. for loop
        for n in nums:
            count[n] += 1
            
            # n // 3 -> 최대 2개만 가능
            if len(count) > 2:
                new_count = defaultdict(int)

                # cnt가 0이거나 1인 경우는 제외
                for n, cnt in count.items():
                    if cnt > 1:
                        new_count[n] = cnt - 1
                
                count = new_count
        
        # 3. 마지막 체크
        res = []
        for n in count.keys():
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res
        