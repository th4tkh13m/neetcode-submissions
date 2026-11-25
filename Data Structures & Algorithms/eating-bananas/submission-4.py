class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The eating speed is between 1 and max pile
        left = 1
        right = max(piles)

        def checkEat(piles, h, k):
            for pile in piles:
                # if pile < k:
                h -= (pile + k - 1) // k
                if h < 0:
                    return False
            return h >= 0

        while left < right:
            mid = left + (right - left) // 2
            if checkEat(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return right            
                