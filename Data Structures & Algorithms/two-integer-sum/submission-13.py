class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 2:
            return [0,1]
        
        remaining_map = {}
        i = 0
        while i < n:
            if nums[i] in remaining_map:
                return [remaining_map[nums[i]], i]

            remaining = target - nums[i]
            remaining_map[remaining] = i
            
            i += 1