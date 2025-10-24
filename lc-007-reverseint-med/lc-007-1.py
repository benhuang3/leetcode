class Solution:
    def reverse(self, x: int) -> int:
        LOWER_BOUND = -2147483648
        UPPER_BOUND = 2147483647
        is_negative = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x > 0:
            res = res * 10 + (x % 10)
            x //= 10
        res = is_negative * res
        return res if LOWER_BOUND <= res <= UPPER_BOUND else 0

        
        