class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        consecutives = []
        start = 0
        max_consecutive = 0

        # Have a hashset so that lookup is O(1)
        # => Check whether num - 1 in hash set or not
        for num in hashset:
            if not num - 1 in hashset:
                start = num
                current = start
                con_length = 0
                while current in hashset:
                    con_length += 1
                    current += 1
                max_consecutive = max(max_consecutive, con_length)
        
        return max_consecutive