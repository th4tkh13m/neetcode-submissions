class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = []
        for num in nums:
            if not num in appeared:
                appeared.append(num)
            else:
                return True
        return False