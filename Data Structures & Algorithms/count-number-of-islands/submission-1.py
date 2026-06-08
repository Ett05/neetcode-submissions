from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    visited = self._bfs_helper((i, j), grid, visited)
                    num_of_islands += 1
        return num_of_islands
        
    def _bfs_helper(self, point, grid, visited):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque([point])
        visited = visited
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc # New row, New column
                
                # Is it within the grid AND is it land?
                if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and (grid[nr][nc] == "1"):
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        return visited 
            
