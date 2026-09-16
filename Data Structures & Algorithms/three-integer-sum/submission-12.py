class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Idea: We can sort the list so that we can use 2 pointers
        # 2 pointers are efficient in term of time and space
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        result = []
        # After sort from asc
        # We have i: running from start to end
        for i in range(n):
            if sorted_nums[i] > 0:
                return result
            if i >= 1 and sorted_nums[i] == sorted_nums[i-1]:
                continue
        # 2 pointers: left, right, running from i + 1 to n
            left, right = i + 1, n - 1
            while left < right:

                while left < right and sorted_nums[i] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                while left < right and sorted_nums[i] + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                if left < right and sorted_nums[i] + sorted_nums[left] + sorted_nums[right] == 0:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1

                while left < right and left > i + 1 and sorted_nums[left] == sorted_nums[left - 1]:
                    left += 1
            
                
        return result
        # If nums[i] + nums[left] + nums[right] > 0 => right -= 1
        # < 0 => left += 1
        # = then add
        # Handle duplicate
        # Since we sorted => If nums[left] = nums[left - 1] => Skip
        # Similar to i as well
