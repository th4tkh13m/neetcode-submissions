class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==0:
            return 0
        
        if n == 1:
            return 1
        
        
        longest = 1

        set_nums = set(nums)


        # Idea: maybe 1 scanner: start from the beginning
        # add visit when face a new char
        # check whether num - 1 in set, if yes, it is a consecutive
        # We also have to somehow track the consecutive count as well

        max_length = 0

        for num in set_nums:
            if num-1 in set_nums:
                continue
            else:
                current = num
                current_length = 0
                while current in set_nums:
                    current += 1
                    current_length += 1

                    max_length = max(max_length, current_length)
        return max_length



        