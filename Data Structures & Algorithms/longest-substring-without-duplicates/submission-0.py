class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        j = 0
        current_len = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            while s[i] in s[j:i]:
                j += 1
                    
            current_len = len(s[j:i+1])
            if max_len < current_len:
                max_len = current_len
        return max_len
