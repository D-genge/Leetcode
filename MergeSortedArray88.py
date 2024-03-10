class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return
        if len(nums1) == 1:
            nums1[0] = nums2[0]
            return
        curr = len(nums1) - 1
        n2 = len(nums2) - 1
        n1 = curr - n2 - 1
        while n1 >= 0 or n2 >= 0:
            if n1 < 0:
                nums1[curr] = nums2[n2]
                n2 -= 1
                curr -= 1
                continue 
            if n2 < 0:
                return
            if nums1[n1] >= nums2[n2]:
                nums1[curr] = nums1[n1]
                curr -= 1
                n1 -= 1
                continue
            if nums2[n2] > nums1[n1]:
                nums1[curr] = nums2[n2]
                curr -= 1
                n2 -= 1
                continue
            