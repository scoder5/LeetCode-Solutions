class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if j == i or j == ROWS-i-1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
                
         