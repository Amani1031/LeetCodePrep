from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Find all zeroes -- do not modify any other 0's
        rowcol = []
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                if matrix[i][k] == 0:
                    rowcol.append((i, k))

        # Modify all ROWS and COLUMNS that are involved with the zero

        for t in rowcol:
            matrix[t[0]] = [0] * len(matrix[0])
            for i in range(len(matrix)):
                matrix[i][t[1]] = 0