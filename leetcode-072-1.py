class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        input_len = len(word1)
        target_len = len(word2)
        steps = [[-1 for _ in range(target_len+1)] for _ in range(input_len+1)]
        for i in range(0, input_len + 1):
            steps[i][target_len] = input_len - i
        for i in range(0, target_len + 1):
            steps[input_len][i] = target_len - i

        def getSteps(row, col):
            if (steps[row][col] == -1):
                if (word1[row] == word2[col]):
                    steps[row][col] = getSteps(row + 1, col + 1);
                else:
                    steps[row][col] = 1 + min(getSteps(row + 1, col), getSteps(row, col + 1), getSteps(row + 1, col + 1))
            return steps[row][col]
        return getSteps(0,0)
solution = Solution()
print(solution.minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine"))