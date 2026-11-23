class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        left = 0
        right = 0
        longest = 0
        visit = set()

        while right < n:
            while s[right] in visit:
                # Moving left to the later of the first dup
                visit.remove(s[left])
                left += 1
            
            # add right to visit, move right
            visit.add(s[right])

            longest = max(longest, right - left + 1)
            right += 1
        return longest
        
        


        