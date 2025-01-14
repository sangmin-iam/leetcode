    # 1. 문제 이해
    # ex) n=4 -> [1, 2, 3, 4], k = 2 -> [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]
    # 2. 설계
    # curNum -> 현재 숫자
    # curCombs -> 현재까지 조합
    # combs -> 정답을 저장할 조합들
    # 3. 구현
    # 4. 디버깅

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        self.helper(1, [], result, n, k)

        return result


    def helper(self, curNum: int, curCombs: List[int], combs: List[List[int]], n, k):
        if len(curCombs) == k:
            combs.append(curCombs.copy())
            return
        if curNum > n:
            return

        for num in range(curNum, n + 1):
            curCombs.append(num)
            self.helper(num + 1, curCombs, combs, n, k)
            curCombs.pop()
