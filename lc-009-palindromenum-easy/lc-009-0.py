class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        xs = xs[::-1]
        for i in range(0, len(xs)):
            if xs[i] != xs[len(xs) - 1 - i]:
                return False
        return True
        