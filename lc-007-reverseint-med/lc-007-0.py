class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1) 
        return res if -2147483648 <= res <= 2147483647 else 0
        