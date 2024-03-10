class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Brute Force o(n^n)
        # def rec (i): 
        #     if i >= len(nums):
        #         return False
        #     if i == len(nums) - 1:
        #         return True
        #     if nums[i] == 0:
        #         return False
            
        #     for j in range(nums[i], 0, -1):
        #         if rec(i + j) == True:
        #             return True
        #     return False
        # return rec(0)
        
        # Greedy o(n)
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= goal - i:
                goal = i

        return goal == 0


        

            