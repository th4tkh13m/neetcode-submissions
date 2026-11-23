class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We maintain a window of 1 character + k other characters

        left = 0
        right = 0
        remaining_replacement = k
        visit_count = {}
        longest = 0
        max_f = 0

        while right < len(s):
            visit_count[s[right]] = visit_count.get(s[right], 0) + 1
            max_f = max(max_f, visit_count[s[right]])


            while right - left + 1 - max_f > k:
                # Start moving the left
                if visit_count[s[left]] > 0:
                    visit_count[s[left]] -= 1
                else:
                    del visit_count[s[left]]
                left += 1


            longest = max(longest, right - left + 1)
            right = right + 1
        return longest


            


