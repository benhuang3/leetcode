class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import heapq

        def printMatrix(matrix):
            for row in matrix:
                print(row)
        input_len = len(word1)
        target_len = len(word2)
        
        #initializating matrix

        visited = [[0 for _ in range(target_len+1)] for _ in range(input_len+1)]
        printMatrix(visited)

        #adds node to fringe, unless already visited
        def addNode(node):
            _weight = node[0]
            _row = node[1]
            _col = node[2]

            if (visited[_row][_col] == 0):
                if (_row == input_len):
                    _weight += target_len - _col
                elif (_col == target_len):
                    _weight += input_len - _row

                heapq.heappush(fringe, (_weight, _row, _col))

        row = 0
        col = 0
        #djikstra's, each one is (weight, row, col)
        fringe = []
        addNode((0, 0, 0))

        #djikstra's algorithm
        while True:
            node = heapq.heappop(fringe)
            weight = node[0]
            row = node[1]
            col = node[2]

            if (row >= len(word1) or col >= len(word2)):
                break

            visited[row][col] = 1

            if (word1[row] == word2[col]):
                addNode((weight, row + 1, col + 1))
            else:
                addNode((weight + 1, row + 1, col))
                addNode((weight + 1, row, col + 1))
                addNode((weight + 1, row + 1, col + 1))

        return weight

solution = Solution()
print(solution.minDistance("", "a"))

