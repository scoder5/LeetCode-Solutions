class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumd, mid = 0, len(mat)//2
        for i in range(len(mat)):
            sumd += mat[i][i]
            sumd += mat[len(mat)-1-i][i]
            
        if len(mat) % 2 == 1:
            sumd -= mat[mid][mid]
            
        return sumd