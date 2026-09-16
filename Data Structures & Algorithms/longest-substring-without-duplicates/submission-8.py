class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Idea: Using sliding window:
        # Left: At the character when the dup is found
        # Right: Continue checking
        if len(s) == 0:
            return 0
        max_len = 0
        left = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            current_len = right - left + 1
            max_len = max(current_len, max_len)
        return max_len