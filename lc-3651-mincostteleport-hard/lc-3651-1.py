class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        inf = float('inf')
        height = len(grid)
        width = len(grid[0])
        min_cost = inf
        min_list = [0 for _ in range(10**4 + 1)]
        dp = [[[inf for _ in range(width)] for _ in range(height)] for _ in range(k+1)]
        dp[k][0][0] = 0
        # def initialize_min_list(layer):
        #     min_exact_list = [inf for _ in range(10**4 + 1)]
        #     for i in range(height):
        #         for j in range(width):
        #             weight = grid[i][j]

        #             min_exact_list[weight] = min(dp[layer][i][j], min_exact_list[weight])

        #     min_list[len(min_exact_list) - 1] = min_exact_list[len(min_exact_list) - 1]
        #     for i in range(len(min_exact_list) - 2, -1, -1):
        #         min_list[i] = min(min_list[i+1], min_exact_list[i])
                                              
        def initialize_min_list(layer):
            value_to_min = {}
            for i in range(height):
                for j in range(width):
                    v = grid[i][j]
                    value_to_min[v] = min(value_to_min.get(v, inf), dp[layer][i][j])
    
            sorted_values = sorted(value_to_min.keys(), reverse=True)
            running_min = inf
            for v in sorted_values:
                running_min = min(running_min, value_to_min[v])
                min_list[v] = running_min

        for i in range(height):
            for j in range(width):
                if i == 0 and j == 0: continue
                
                dp[k][i][j] = grid[i][j] + min(
                    dp[k][i-1][j] if i else inf, 
                    dp[k][i][j-1] if j else inf
                    )
                if i == height - 1 and j == width - 1:
                    min_cost = dp[k][i][j]
        
        for t in range(k-1, -1, -1):
            initialize_min_list(t + 1)
            for i in range(height):
                for j in range(width):
                    if i == 0 and j == 0:
                        dp[t][i][j] = 0
                        continue
                    dp[t][i][j] = min(
                        grid[i][j] + dp[t][i-1][j] if i else inf,
                        grid[i][j] + dp[t][i][j-1] if j else inf,
                        min_list[grid[i][j]]
                        )
                    if i == height - 1 and j == width - 1:
                        min_cost = min(min_cost, dp[t][i][j])

        return min_cost



        
            

