class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1

        while l <= r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1

        """
        Do not return anything, modify s in-place instead.
        """
        