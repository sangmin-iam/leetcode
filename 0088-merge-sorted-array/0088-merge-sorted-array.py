class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m - 1
        r = n - 1
        now = len(nums1) - 1

        while l >= 0 and r >= 0:
            if nums1[l] >= nums2[r]:
                nums1[now] = nums1[l]
                l -= 1
            else:
                nums1[now] = nums2[r]
                r -= 1
            now -= 1
        
        while r >= 0:
            nums1[now] = nums2[r] 
            r -= 1
            now -= 1
