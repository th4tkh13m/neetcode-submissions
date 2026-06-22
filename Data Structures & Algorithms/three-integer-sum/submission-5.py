class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        results = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            l = i + 1
            r = len(nums) - 1

            if i> 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            while l < r:
                if sorted_nums[i] + sorted_nums[l] + sorted_nums[r] < 0:
                    l += 1
                    continue
                elif sorted_nums[i] + sorted_nums[l] + sorted_nums[r] > 0:
                    r -= 1
                    continue
                else:
                    results.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1 
                    r -= 1

                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
                
        return results
