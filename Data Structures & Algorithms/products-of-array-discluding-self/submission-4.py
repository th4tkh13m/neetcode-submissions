class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Idea: Have 2 arrays multiplying from 2 sides
        # left[i] = left[0] *...* left[i-1]
        # right[i] = right[-1] *...* left[i+1]
        n = len(nums)
        left, right  = [1] * n, [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] *nums[i - 1]
        
        for i in range(n-2, -1, -1):
            right[i] = right[i + 1] *nums[i + 1]

        result = []
        for i in range(n):
            result.append(left[i] * right[i])
        return result        
         
        