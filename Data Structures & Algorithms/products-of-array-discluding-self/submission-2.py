class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_matrix, right_matrix = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            left_matrix[i] = left_matrix[i - 1] * nums[i - 1]
            right_matrix[len(nums)  - 1 - i] = right_matrix[len(nums) - i] * nums[len(nums) - i]

        for i in range(len(nums)):
            left_matrix[i] *= right_matrix[i]
        return left_matrix