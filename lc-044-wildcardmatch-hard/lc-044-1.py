class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        str_index = 0
        def matchChar(expr_c, str_c):
            return expr_char == '?' or expr_c == str_c
        for c in p:
            pass