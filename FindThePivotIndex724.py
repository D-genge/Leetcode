class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arraySum = sum(nums)
        currCount = 0 
        
        for i in range(len(nums)):
            currTarget = arraySum - nums[i]

            if currCount == currTarget / 2:
                return i
            currCount += nums[i]
        return -1