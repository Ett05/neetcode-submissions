class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_grid = [[0 for i in range(n)] for i in range(m)]
        dp_grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    dp_grid[i][j] = dp_grid[i-1][j] 
                elif i == 0:
                    dp_grid[i][j] = dp_grid[i][j-1] 
                else:
                    dp_grid[i][j] = dp_grid[i][j-1] + dp_grid[i-1][j] 
        return dp_grid[-1][-1]
