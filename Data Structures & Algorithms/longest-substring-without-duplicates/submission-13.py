class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        left = 0
        right = 0
        max_longest = 0
        visit = set()
        while right < len(s):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1
    
            visit.add(s[right])
            
            max_longest = max(max_longest, right - left + 1)
            right += 1
        return max_longest

        