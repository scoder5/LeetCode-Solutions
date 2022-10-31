class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j not in groups:
                    groups[i-j] = matrix[i][j]
                elif groups[i-j] != matrix[i][j]:
                    return False
        return True