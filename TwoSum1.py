class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            missing = target - nums[i]
            
            if missing in hmap:
                return [hmap[missing], i]

            if nums[i] not in hmap:
                hmap[nums[i]] = i
