# 1. 문제 이해
# - 6과 9로만 이루어진 숫자
# - 0~1번 숫자 변경 가능
# - 최대 숫자 리턴하기

# 2. 문제 설계
# - 가장 왼쪽부터 보면서 6이 있으면 9로 변경
# - 이 작업을 위해서 String으로 변경 필요

class Solution:
    def maximum69Number (self, num: int) -> int:
        numList = list(str(num)) # O(n)

        for i, char in enumerate(numList): # O(n)
            if char == '6':
                numList[i] = '9'
                break
        
        return int("".join(numList)) # O(n)
