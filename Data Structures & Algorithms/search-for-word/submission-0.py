from collections import deque 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self._dfs_helper((i, j), board, len(board), len(board[i]), word):
                        return True
        return False

        
    def _dfs_helper(self, point, board, height, width, word):
        counter = 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        stack = [(point, 1, {point})]

        while stack:
            point, counter, visited = stack.pop()

            if counter == len(word):
                return True

            for dr, dc in directions:
                nr, nc = point[0] + dr, point[1] + dc
                if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in visited and board[nr][nc] == word[counter]:
                    stack.append(((nr, nc), counter + 1, visited | {(nr, nc)}))

        return False
        print(counter)
        return counter == len(word)