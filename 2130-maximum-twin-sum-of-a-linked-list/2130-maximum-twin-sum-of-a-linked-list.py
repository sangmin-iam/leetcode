# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None 

        # 중간 지점을 찾으러 가면서 중간 전까지 코드는 리버스
        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next # 기존 다음 노드 저장
            slow.next = prev # 현재 노드을 리버스
            prev = slow # 현재 노드 기억
            slow = temp # 다음 진행할 노드 저장
        
        # 중간 2개 지점에서 양쪽으로 뻗어가면서 결과값을 구함
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return res
        