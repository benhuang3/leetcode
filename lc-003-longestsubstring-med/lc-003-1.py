class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        best = 0
        start = 0

        for i, char in enumerate(s):
            span = i - start
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            if span > best:
                best = span
            seen[char] = i
        
        return max(best, len(s) - start)