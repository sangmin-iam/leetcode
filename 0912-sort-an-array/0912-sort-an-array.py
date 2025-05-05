# Merge Sort
# TC: O(n log n)
# SC: O(n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: List[int], L: int, M:int, R: int):
            # 왼쪽 배열
            left = arr[L:M + 1]
            # 오른쪽 배열
            right = arr[M + 1:R + 1]
            i = L # 원본 배열 인덱스
            j = 0 # 왼쪽 배열 인덱스
            k = 0 # 오른쪽 배열 인덱스

            # 기본 삽입 로직
            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
    
                i += 1
            # 왼쪽 배열이 남아있는 경우
            while j < len(left):
                nums[i] = left[j]
                i += 1
                j += 1
            
            # 오른쩍 배열이 남아있는 경우
            while k < len(right):
                nums[i] = right[k]
                i += 1
                k += 1
            

        def mergeSort(arr: List[int], l: int, r: int) -> None:
            if l == r:
                return

            mid = (l + r) // 2 # 중앙을 기준으로 나눔  (int)
            
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            merge(arr, l, mid, r)
            return            

        mergeSort(nums, 0, len(nums))
        
        return nums
