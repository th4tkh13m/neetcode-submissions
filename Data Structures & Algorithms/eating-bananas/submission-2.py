class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        n = len(piles)

        max_pile = max(piles)

        # Time should be ranging from 0 -> max pile

        def checkEat(piles, h, k):
            for pile in piles:
                h -= math.ceil(pile / k)
            return h >= 0
        
        left = 1
        right = max_pile

        while left < right:
            mid = left + (right - left) // 2
            if checkEat(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        
        return right
                