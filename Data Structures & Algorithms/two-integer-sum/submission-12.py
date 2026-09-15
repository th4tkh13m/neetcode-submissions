class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea: Loop over the list, and save the needed value to the current index
        remaining = {}
        for i in range(len(nums)):
            current = nums[i]
            if current in remaining:
                return [remaining[current], i]

            needed = target - nums[i]
            remaining[needed] = i