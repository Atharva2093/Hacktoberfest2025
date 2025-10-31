class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l = 0
        r = len(matrix) - 1

        # 1. Reverse the rows of the matrix
        while l < r:
            # Swap matrix[l] and matrix[r]
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # 2. Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i):
                # Swap matrix[i][j] and matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
