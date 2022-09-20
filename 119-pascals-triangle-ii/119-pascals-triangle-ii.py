class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pt = [[1] * (i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1, i):
                pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
                
        return pt[rowIndex]