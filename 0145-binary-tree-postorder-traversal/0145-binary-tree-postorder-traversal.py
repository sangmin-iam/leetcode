# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visit = [False]

        while stack:
            currentNode = stack.pop()
            visited = visit.pop()
            
            if currentNode:
                if visited: # 방문한게 True라면 왼쪽 오른쪽 노드를 이미 스택에 등록한 것을 의미
                    res.append(currentNode.val)
                else:
                    stack.append(currentNode)
                    visit.append(True)
                    stack.append(currentNode.right)
                    visit.append(False)
                    stack.append(currentNode.left)
                    visit.append(False)

        return res