class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_idx = {}
        for idx, num in enumerate(nums):
            if not num in to_idx:
                to_idx[num] = [idx]
            else:
                to_idx[num].append(idx)
        for idx, num in enumerate(nums):
            other = target - num
            if other in to_idx:
                if other == num and len(to_idx[num]) == 1:
                    continue
                else:
                    return [idx, max(to_idx[other])]


        