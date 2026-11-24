class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]: 
                if nums[mid] < nums[right]:
                    if target <= nums[right]:
                    # Correct, search the rhs
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                #     # mid > right => result still on right?
                        # for sure
                    left = mid + 1
            else:
                if nums[mid] < nums[right]:
                # target < mid
                # mid < right  => search on the left for sure
                    right = mid - 1
                else:
                # target < mid, mid > right => search on left
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return -1
