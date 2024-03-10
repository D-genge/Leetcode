class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n, m = n - 1, m - 1
        curr = n - m - 1
        if not nums1 or not nums2:
            return
        if len(nums1) == 1:
            nums1[0] = nums2[0]
            return
        while m >= 0 or n >= 0:
            if n < 0:
                nums1[curr] = nums2[m]
                m -= 1
                curr -= 1
            elif nums1[n] >= nums2[m]:
                nums1[curr] = nums1[n]
                curr -= 1
                n -= 1

            if nums2[m] > nums1[n]:
                nums1[curr] = nums2[m]
                curr -= 1
                m -= 1
                continue
            