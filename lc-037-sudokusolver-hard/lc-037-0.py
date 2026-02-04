class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        answered = False

        def allowed_nums(y, x):
            
            nums = {'1','2','3','4','5','6','7','8','9'}
            for i in range(0, 9):
                if board[i][x] in nums:
                    nums.remove(board[i][x])
                if board[y][i] in nums:
                    nums.remove(board[y][i])
            y_corner = int(y / 3) * 3
            x_corner = int(x / 3) * 3
            for i in range(y_corner, y_corner + 3):
                for j in range(x_corner, x_corner + 3):
                    if board[i][j] in nums:
                        nums.remove(board[i][j])
            return nums
        print("starting")
        def dp(i, j):
            nonlocal answered
            if answered: return
            
            if i == 9: 
                answered = True
                print("answer found")
                print(board)
                return
            if j == 9: 
                dp(i+1, 0)
                return

            if board[i][j] != '.': 
                dp(i, j+1)
                return

            nums = allowed_nums(i,j)
            # print(f"({i}, {j}), {nums}")
            if not nums:
                return
            for num in nums:
                if answered: return
                board[i][j] = num
                dp(i, j+1)
            if not answered:
                board[i][j] = '.'  # backtrack only if not solved
        dp(0,0)




        