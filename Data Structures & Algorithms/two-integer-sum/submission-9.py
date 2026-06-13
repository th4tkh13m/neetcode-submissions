class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_idx = {}
        for i in range(len(nums)):
            if (target - nums[i]) in to_idx:
                return [to_idx[target - nums[i]], i]
            if not nums[i] in to_idx:
                to_idx[nums[i]] = i

        