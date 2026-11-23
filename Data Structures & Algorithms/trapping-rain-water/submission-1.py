class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]

        water = 0
        current = left
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            water += (max(0, min(left_max, right_max) - height[current]))

            if height[left] <= height[right]:
                left += 1
                current = left
            else:
                right -= 1
                current = right
        return water