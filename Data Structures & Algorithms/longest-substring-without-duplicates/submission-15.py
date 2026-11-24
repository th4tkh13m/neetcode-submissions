class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        # We store the set of visit characters
        # We will maintain the window with non dup chars, when we find the char, we slide the left over the first dup
        # still store the longest substring

        longest_substring = 0
        visit = set()

        left = 0
        right = 0

        while right < n:
            while s[right] in visit:
                # start sliding
                visit.remove(s[left])
                left += 1
            visit.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)
            right += 1
        
        return longest_substring
        
        


        