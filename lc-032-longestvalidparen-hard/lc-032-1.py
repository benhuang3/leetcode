class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left_paren_stack = [-1]
        max_len = 0

        for i, c in enumerate(s):
            if c == "(":
                left_paren_stack.append(i)
            elif c == ")":
                left_paren_stack.pop()
                if len(left_paren_stack) == 0:
                    left_paren_stack.append(i)
                max_len = max(max_len, i - left_paren_stack[-1])
        return max_len
        