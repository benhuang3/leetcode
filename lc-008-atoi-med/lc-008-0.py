class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        reading_whitespace = True
        read_sign = False
        reading_leading_zero = True

        numbers = ("0","1","2","3","4","5","6","7","8","9")
        signs = ("+", "-")
        sign = 1
        for c in s:
            if c in numbers:
                reading_whitespace = False
                read_sign = True
                if c == 0 and reading_leading_zero:
                    continue
                else:
                    reading_leading_zero = False
                    res = res * 10 + int(c)
            elif c in signs and not read_sign:
                reading_whitespace = False
                read_sign = True
                sign = -1 if c == "-" else 1
            elif c == " " and reading_whitespace:
                continue
            else:
                break
        res = res * sign
        res = min(res, 2 ** 31 - 1)
        res = max(res, -(2 ** 31))

        return res

        