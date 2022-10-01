class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        def isDiagonal(i, j, ROWS):
            return (i == j) or (i + j == ROWS - 1)
        
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if isDiagonal(i, j, ROWS):
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
                
         