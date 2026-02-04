class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        def box_idx(i, j):
            return (i // 3) * 3 + (j // 3)

        # Initialize masks from existing board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    bit = 1 << (int(board[i][j]) - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[box_idx(i, j)] |= bit

        def dp(i, j):
            if i == 9:
                return True
            if j == 9:
                return dp(i + 1, 0)
            if board[i][j] != '.':
                return dp(i, j + 1)

            b = box_idx(i, j)
            available = ~(rows[i] | cols[j] | boxes[b]) & 0x1FF

            while available:
                bit = available & -available  # lowest set bit
                digit = bit.bit_length()      # 1-9

                # place digit
                board[i][j] = str(digit)
                rows[i] |= bit
                cols[j] |= bit
                boxes[b] |= bit

                if dp(i, j + 1):
                    return True

                # backtrack
                board[i][j] = '.'
                rows[i] &= ~bit
                cols[j] &= ~bit
                boxes[b] &= ~bit

                available &= available - 1  # clear lowest bit

            return False

        dp(0, 0)
