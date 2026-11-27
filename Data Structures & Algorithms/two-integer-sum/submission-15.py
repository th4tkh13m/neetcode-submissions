class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, val in enumerate(nums):
            if val in index_map:
                return [index_map[val], i]
            remaining = target - val
            index_map[remaining] = i
        

            
