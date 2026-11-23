class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We maintain a window of 1 character + k other characters

        left = 0
        right = 0
        remaining_replacement = k
        visit_count = {}
        longest = 0

        while right < len(s):
            visit_count[s[right]] = visit_count.get(s[right], 0) + 1
            remaining_placement = k - (right - left + 1 - max(visit_count.values()))

            while remaining_placement < 0:
                # Start moving the left
                if visit_count[s[left]] > 0:
                    visit_count[s[left]] -= 1
                else:
                    del visit_count[s[left]]
                left += 1
                remaining_placement = k - (right - left + 1 - max(visit_count.values()))


            longest = max(longest, right - left + 1)
            right = right + 1
        return longest


            


