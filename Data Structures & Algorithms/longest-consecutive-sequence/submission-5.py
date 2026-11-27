class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Turn to set
        # Loop over the set, check whether i + 1 in set,
        # If not, continue
        longest = 0
        set_num = set(nums)

        for val in set_num:
            if not val - 1 in set_num:
                length = 0
                current = val
                while current in set_num:
                    length += 1
                    current += 1
                longest = max(longest, length)
        
        return longest

