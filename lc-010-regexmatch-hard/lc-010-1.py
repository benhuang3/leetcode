class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matchChar(expr_c, str_c):
            if str_c == ';':
                return False
            if expr_c == '.':
                return True
            else:
                return expr_c == str_c
        def isModifier(expr_i):
            return p[expr_i + 1] == "*" if expr_i + 1 < len(p) else False

        def tokenize():
            expr_i = 0
            tokens = []
            while expr_i < len(p):
                expr_char = p[expr_i]
                if isModifier(expr_i):
                    expr_char = expr_char + "*"
                    expr_i += 1
                tokens.append(expr_char)
                expr_i += 1 
            return tokens
        def isStar(expr):
            return expr[0] if len(expr) > 1 else None
        s = s + ';'
        tokens = tokenize()
        dp = [[False for _ in range(len(tokens) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True if isStar(tokens[0]) else matchChar(tokens[0], s[0]) 

        for i in range(len(s)):
            for j in range(len(tokens)):

                if dp[i][j]:
                    str_char = s[i]
                    expr_char = tokens[j]

                    if matchChar(expr_char[0], str_char):
                        dp[i+1][j+1] = True
                    if isStar(tokens[j]):
                        dp[i][j+1] = True
                        if matchChar(expr_char[0], str_char):
                            dp[i+1][j] = True
        for row in dp:
            print(row)
        return dp[len(s) - 1][len(tokens)]
        