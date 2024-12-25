# 1. 문제 이해
# - pivot index가 존재, 이 인덱스를 기준 왼쪽합/오른쪽합이 같아야함
# - 가장 왼쪽에 존재하는 pivot 인덱스 구하기
# 2. 분석 및 설계
# - prefix 구하기
# - 오른쪽에서 왼쪽으로 가면서 마지막에 선택된 pivot 인덱스 사용
# 3. 구현
# 4. 디버깅

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = -1
        # 1. Prefix 구하기
        prefix = []
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i - 1] + nums[i])
        
        # 2. 오른쪽에서 왼쪽으로 1씩 내려가면서, 마지막에 찾은 pivot index 리턴
        for i in range(len(nums) - 1, -1, -1):
            leftSum = 0 if i == 0 else prefix[i - 1]
            rightSum = 0 if i == len(nums) - 1 else prefix[len(nums) - 1] - prefix[i]
            
            if leftSum == rightSum:
                result = i

        return result
        
        