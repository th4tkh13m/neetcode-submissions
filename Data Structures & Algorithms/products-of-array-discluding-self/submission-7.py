class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        postfix_prod = [1] * len(nums)
        result = []
        for i in range(1, len(nums)):
            prefix_prod[i] *= prefix_prod[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            postfix_prod[i] *= postfix_prod[i+1] * nums[i+1] 
        
        for i in range(len(nums)):
            result.append(prefix_prod[i] * postfix_prod[i])
        return result