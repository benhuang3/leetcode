class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        inf = float('inf')
        height = len(grid)
        width = len(grid[0])
        min_cost = inf
        min_list = [0 for _ in range(10**4) + 1]
        dp = [[[inf for _ in range(width)] for _ in range(height)] for _ in range(k+1)]
        dp[k][0][0] = 0

                                                     
        def minimum_teleport_cost(layer, weight):
            cur_min = inf
            for i in range(height):
                for j in range(width): 
                    if grid[i][j] < weight: continue

                    if grid[i][j] >=  weight and dp[layer + 1][i][j] < cur_min:
                        cur_min = dp[layer + 1][i][j]
            return cur_min
            
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
            for i in range(height):
                for j in range(width):
                    if i == 0 and j == 0:
                        dp[t][i][j] = 0
                        continue
                    dp[t][i][j] = min(
                        grid[i][j] + dp[t][i-1][j] if i else inf,
                        grid[i][j] + dp[t][i][j-1] if j else inf,
                        minimum_teleport_cost(t, grid[i][j])
                        )
                    if i == height - 1 and j == width - 1:
                        min_cost = min(min_cost, dp[t][i][j])

        return min_cost



        
            

