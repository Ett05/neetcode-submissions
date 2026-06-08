from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        queue = deque()
        time = 0
        fresh_fruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_fruit += 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh_fruit > 0:
            for i in range(len(queue)):
                point = queue.popleft()
                print(point)
                for direction in directions:
                    nr,nc = direction
                    new_r = nr + point[0]
                    new_c = nc + point[1]
                    if new_r >= 0 and new_r < height and new_c >= 0 and new_c < width:
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            queue.append((new_r,new_c))
                            fresh_fruit -= 1 
            time += 1
            # points = queue.popleft()
            # print(points)
            # print(time)
            # for point in points:
            #     # print(point)
            #     list_to_append = []
                # for direction in directions:
                #     nr,nc = direction
                #     new_r = nr + point[0]
                #     new_c = nc + point[1]
                #     if new_r >= 0 and new_r < height and new_c >= 0 and new_c < width:
                #         if grid[new_r][new_c] == 1:
                #             grid[new_r][new_c] = 2
                #             list_to_append.append((new_r,new_c))
                #             fresh_fruit -= 1 
            #     if list_to_append: queue.append(list_to_append) 
            #     print(queue)


            # time += 1
        
        if fresh_fruit != 0:
            return -1
        else:
            return time