class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        def cc(mat, i, j, ROWS, COLS):
            for var in range(ROWS):
                if var != i:
                    if mat[var][j] == 1:
                        return False
            return True
        
        def cr(mat, i, j, ROWS, COLS):
            for var in range(COLS):
                if var != j:
                    if mat[i][var] == 1:
                        return False
            return True
        
        ROWS, COLS = len(mat), len(mat[0]) 
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 1 and (cr(mat,i,j,ROWS,COLS) and cc(mat,i,j,ROWS,COLS)):
                    count += 1
        return count        