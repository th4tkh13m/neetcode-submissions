class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backward = []
        list_len = len(nums)
        start_forward = 1
        start_backward = 1
        i=0
        while i in range(len(nums)):
            start_forward *= nums[i]
            start_backward *= nums[list_len - i -1]

            forward.append(start_forward)
            backward.append(start_backward)
            i+=1
        arr = []
        for i in range(len(nums)):
            if i == 0:
                val = backward[list_len - 2]
            elif i == (list_len - 1):
                val = forward[list_len - 2]
            else:
                val = forward[i-1] * backward[list_len - i -2]
            arr.append(val)
            i+=1
        return arr