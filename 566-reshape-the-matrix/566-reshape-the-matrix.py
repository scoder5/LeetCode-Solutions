class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if not m*n == r*c: return mat
        OneD = [mat[i][j] for i in range(m) for j in range(n)]
        return [OneD[i*c:(i+1)*c] for i in range(r)]
                