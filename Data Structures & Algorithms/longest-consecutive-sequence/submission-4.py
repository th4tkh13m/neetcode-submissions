class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Turn to set
        # Loop over the set, check whether i + 1 in set,
        # If not, continue
        longest = 0
        set_num = set(nums)

        while set_num:
            current = min(set_num)
            length = 0
            while current in set_num:
                length += 1
                set_num.remove(current)
                current += 1
            longest = max(longest, length)
        
        return longest

