class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left_paren_stack = [-1]
        matched = [0] * len(s)
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                left_paren_stack.append(i)
            elif c == ")":
                if len(left_paren_stack) != 0:
                    left_paren = left_paren_stack.pop()
                    matched[left_paren] = 1
                    matched[i] = 1

        max_len = 0
        cur_len = 0
        for i in matched:
            if i == 0:
                cur_len = 0
            elif i == 1:
                cur_len += 1

            if cur_len > max_len:
                max_len = cur_len
        return max_len
            


            
        