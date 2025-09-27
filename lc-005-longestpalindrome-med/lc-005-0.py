class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        def subPalinOdd(index):
            start = index - 1
            end = index + 1            
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1: end]

        def subPalinEven(index):
            start = index - 1
            end = index
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1: end]

            
        for i in range(0, len(s)):   
            max_str = max([max_str, subPalinEven(i), subPalinOdd(i)], key = len)  
        return max_str