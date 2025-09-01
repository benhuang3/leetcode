from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = deque()
        seen = set()
        max_substring = 0
        def delete_until_char(c):
            while seen:
                deleted = current_string.popleft()
                seen.remove(deleted)
                if (deleted == c):
                    return

        for char in s:
            if char in seen:
                max_substring = max(max_substring, len(current_string))
                delete_until_char(char)

            current_string.append(char)
            seen.add(char)
        
        max_substring = max(max_substring, len(current_string))
        return max_substring