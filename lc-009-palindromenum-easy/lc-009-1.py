import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        left_exp = int(math.log10(x))
        right_exp = 0

        while left_exp >= right_exp:
            left_digit = x // (10 ** left_exp) % 10
            right_digit = x // (10 ** right_exp) % 10
            
            if (left_digit != right_digit):
                return False
            
            left_exp -= 1
            right_exp += 1
        return True
        