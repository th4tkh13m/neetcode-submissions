class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can try to calculate the backward pass first
        # back[i] = nums[i+1] * back[i+1]
        # We can perform forward[i] = forward[i-1] * back[i]
        n = len(nums)
        forward, backward = [1] * n, [1] * n
        # Skip the final one
        for i in range(n-2, -1,-1):
            backward[i] = backward[i + 1] * nums[i + 1]
        print(backward)
        current = 1
        
        for i in range(n):
            forward[i] = current * backward[i]
            current *= nums[i]
        return forward

