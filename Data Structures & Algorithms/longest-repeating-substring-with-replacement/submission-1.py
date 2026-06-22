class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hashmap of count
        # determine the most repeated one ,others are the one can be replaced with k
        # If exceed => move left pointer to the first one can be replaced with k
        char_counts = [0] * 26
        l = 0
        res =0
        maxf = 0
        for r in range(len(s)):
            char_counts[ord(s[r]) - ord("A")] += 1
            maxf = max(maxf,  char_counts[ord(s[r]) - ord("A")])
            while (r - l + 1) - maxf > k:
                char_counts[ord(s[l]) - ord("A")] -= 1
                l += 1
            res = max(res,r-l+1)
        return res