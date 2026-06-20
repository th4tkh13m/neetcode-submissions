class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}

        for i, val in enumerate(nums):
            remaining = target - val
            
            if val in val_to_index:
                return [val_to_index[val], i]
            
            val_to_index[remaining] = i

        return [0,0]