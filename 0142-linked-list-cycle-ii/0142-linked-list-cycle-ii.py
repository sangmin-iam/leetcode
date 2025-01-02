# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 사이클 찾기
        slow1 = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow1 = slow1.next
            
            # 2. 교차 지점 찾기
            if fast == slow1:
                break

        # 3. 사이클 없는 경우 None 리턴
        if not fast or not fast.next:
            return None
    
        # 4. 사이클 시작 지점 헤드 찾기
        slow2 = head
        while slow2 and slow2.next:
            if slow2 == slow1:
                return slow2

            slow2 = slow2.next
            slow1 = slow1.next

        