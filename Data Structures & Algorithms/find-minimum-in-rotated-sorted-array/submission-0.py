class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mid = right + left / 2
        # if mid < right : good (we save mid), and start search from left -> mid
        # if mid > right: we jump to higher  => search from mid + 1 to right

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2


            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[mid]