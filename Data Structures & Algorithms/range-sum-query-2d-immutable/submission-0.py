class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # Create a prefix sum matrix with an extra row and column of zeros for boundary padding
        self.sumMat = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                # Current prefix sum = current row running sum + sum from the row directly above
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Shift coordinates by +1 because of our padded prefix matrix
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]
        
        return bottomRight - above - left + topLeft