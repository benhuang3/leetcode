from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = s + '!'
        p = p + '!'
        def matchChar(expr_c, str_c):
            if expr_c == '.':
                return True
            else:
                return expr_c == str_c
        def isModifier(expr_i):
            return p[expr_i + 1] == "*" if expr_i + 1 < len(p) else False
        
        @cache
        def handleExpr(expr_i, str_i, star_modifier):            
            if expr_i >= len(p) or str_i >= len(s):
                return expr_i == len(p) and str_i == len(s)
            str_char = s[str_i]
            expr_char = p[expr_i]


            if star_modifier:
                if matchChar(star_modifier, str_char) and (matchChar(expr_char, str_char) or isModifier(expr_i)):
                    return handleExpr(expr_i, str_i, "") or handleExpr(expr_i, str_i + 1, star_modifier)
                elif matchChar(star_modifier, str_char) and not matchChar(expr_char, str_char):
                    return handleExpr(expr_i, str_i + 1, star_modifier)
                else:
                    return handleExpr(expr_i, str_i, "")      
            else:
                if isModifier(expr_i):
                    return handleExpr(expr_i + 2, str_i, expr_char)
                elif not matchChar(expr_char, str_char):
                    return False
                else:
                    return handleExpr(expr_i + 1, str_i + 1, "")
                
        return handleExpr(0, 0, "")
