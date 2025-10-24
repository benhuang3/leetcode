class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = ""
        
        for cur_row in range(0, numRows):
            cur_index = cur_row
            on_diagonal = False

            res = res + s[cur_index]

            while True:
                
                if on_diagonal:
                    to_next_index = 2 * cur_row

                elif not on_diagonal:
                    to_next_index = 2 * (numRows - 1 - cur_row)
                
                cur_index += to_next_index

                if cur_index >= len(s):
                    break

                if to_next_index != 0:
                    res = res + s[cur_index]
                on_diagonal = not on_diagonal
        return res