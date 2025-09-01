class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        def matchChar(expr_c, str_c):
            return expr_char == '?' or expr_c == str_c
        for i in range(len(s)):
            for j in range(len(p)):
                if dp[i][j]:
                    str_char = s[i]
                    expr_char = p[j]
                    if expr_char == '*':
                        dp[i][j+1] = True
                        dp[i+1][j] = True
                    elif matchChar(expr_char, str_char):
                        dp[i+1][j+1] = True
        for i in range(0, len(p) + 1):
            if dp[len(s)][i] and p[i] == '*':
                dp[len(s)][i+1] = True
        return dp[len(s)][len(p)]