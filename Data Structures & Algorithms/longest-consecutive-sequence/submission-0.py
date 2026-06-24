class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        consecutives = []
        start = 0

        # Have a hashset so that lookup is O(1)
        # => Check whether num - 1 in hash set or not
        for num in hashset:
            if not num - 1 in hashset:
                start = num
                current = start
                consecutives.append([])
                while current in hashset:
                    consecutives[-1].append(current)
                    current += 1
        
        max_consecutive = 0
        for con in consecutives:
            max_consecutive = max(max_consecutive, len(con))
        
        return max_consecutive