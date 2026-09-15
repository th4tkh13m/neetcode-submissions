class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Because sorted non decreasing order
        # 2 pointers, 1 from start, 1 from end
        # l <= r
        n = len(numbers)
        right = n - 1
        left = 0
        while left < right:
            while left < right and numbers[left] + numbers[right] > target:
                # reduce
                right -= 1
            while left < right and numbers[left] + numbers[right] < target:
                left += 1
            
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
