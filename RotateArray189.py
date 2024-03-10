class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseSub(start, end):
            while start <= end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1

        k = k % len(nums)
        nums.reverse() # O(n)
        reverseSub(0, k - 1) # O(n) only part of array
        reverseSub(k, len(nums) - 1) # O(n) rest of array