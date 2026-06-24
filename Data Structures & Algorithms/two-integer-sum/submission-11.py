class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}
        for idx, num in enumerate(nums):
            if num in val_idx:
                return [val_idx[num], idx]
            remaining = target - num
            val_idx[remaining] = idx
        