class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_idx = {}
        for idx, num in enumerate(nums):
            if target - num in to_idx:
                return [to_idx[target- num], idx]
            if not num in to_idx:
                to_idx[num] = idx
            


        