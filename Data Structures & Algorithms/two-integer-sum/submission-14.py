class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        remaining_map = {}

        for i, val in enumerate(nums):
            remaining = target - val
            
            if remaining in remaining_map:
                return [remaining_map[remaining], i]
            
            remaining_map[val] = i