class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_mult = 1
        r_mult = 1
        l = [0] * n
        r = [0] * n
        res = [0] * n
        
        for i in range(n):
            j = -i - 1
            l[i] = l_mult
            l_mult *= nums[i]
            r[j] = r_mult
            r_mult *= nums[j]
        
        for i in range(n):
            res[i] = l[i] * r[i]
            
        return res