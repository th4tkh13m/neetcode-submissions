class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2:
            return nums[::-1]
        
        left_array = [1] * n
        right_array = [1] * n

        for i in range(1, n):
            left_array[i] = left_array[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            right_array[i] = right_array[i+1] * nums[i+1]
        result = []
        for i in range(n):
            result.append(left_array[i] * right_array[i])
        
        return result