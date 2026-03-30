# TC: log n + log m = O(log n * m)
# SC: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Find the row: O(log n)
        top = 0
        bottom = len(matrix) - 1
        targetRow = -1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                targetRow = mid
                break
        
        if targetRow == -1:
            return False
        
        # 2. Find the target in the row: O(log m)
        left = 0
        right = len(matrix[0])

        while left <= right:
            mid = (left + right) // 2

            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
