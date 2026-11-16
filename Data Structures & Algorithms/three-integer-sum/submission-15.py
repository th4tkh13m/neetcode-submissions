class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []
        result = []

        sorted_nums = sorted(nums)
        
        for i in range(n):
            left = i + 1
            right = n - 1

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue


            while left < right:
                while left < right and sorted_nums[i] + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                while left < right and sorted_nums[i] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                while left < right and sorted_nums[i] + sorted_nums[left] + sorted_nums[right] == 0:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
        return result
        
                    


        
