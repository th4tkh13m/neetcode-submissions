class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        for j in range(len(s)):

            while s[j] in s[i:j]:
                i += 1
            max_len = max(max_len, j - i + 1)
        
        return max_len