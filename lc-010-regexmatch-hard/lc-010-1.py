class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matchChar(expr_c, str_c):
            if expr_c == '.':
                return True
            else:
                return expr_c == str_c
        def isModifier(expr_i):
            return p[expr_i + 1] == "*" if expr_i + 1 < len(p) else False


        temp_index = 0
        expr_index = 0
        str_index = 0
        star_modifier = ''

        while str_index < len(s):
            str_char = s[str_index]

            if star_modifier:
                temp_char = p[temp_index]
                if isModifier(temp_index):
                    star_modifier = temp_char
                    temp_index = expr_index + 1
                else:
                    if matchChar(temp_char, str_char):
                        if matchChar(star_modifier, str_char):
                            temp_index += 1
                        else:
                            pass
                    else:
                        return False            
                
            else:
                expr_char = p[expr_index]
                if isModifier(expr_index):
                    star_modifier = expr_char
                    expr_index += 1
                    temp_index = expr_index + 1
                    str_index -= 1

                elif not matchChar(expr_char, str_char):
                    return False
                
                expr_index += 1
                str_index += 1

        return expr_index == len(p)

solution = Solution()
print(solution.isMatch('aaa', 'aa..'))