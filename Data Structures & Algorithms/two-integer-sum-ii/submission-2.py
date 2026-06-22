class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        if len(numbers) == 2:
            return [1, 2]
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
                continue
            if numbers[i] + numbers[j] > target:
                j -= 1
                continue
            return [i + 1, j + 1]
        