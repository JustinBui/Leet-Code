# Solution: https://www.youtube.com/watch?v=T41rL0L3Pnw

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])

        zerosOnFirstRow = False

        # Finding which rows and cols contain 0's and marking 0's on 1st rows and columns
        # as markers that there are 0's found on the matrix
        for r in range(row):
            for c in range(col):
                if (matrix[r][c] == 0):
                    matrix[0][c] = 0  # Indices of first row

                    if (r > 0):
                        matrix[r][0] = 0    # Indices of first column
                    else:
                        zerosOnFirstRow = True

        # Filling in 0's relative to first rows and columns on matrix
        for r in range(1, row):
            for c in range(1, col):
                if (matrix[r][0] == 0 or matrix[0][c] == 0):
                    matrix[r][c] = 0

        # Filling the first rows and columns located outside the borders
        # with 0 if possible

        if (matrix[0][0] == 0):
            # Filling in first column (Vertically)
            for i in range(row):
                matrix[i][0] = 0

        if (zerosOnFirstRow):
            # If zeros are originally found on the first row, we gotta fill
            # the entire first row with 0's... But if not, then this cannot happen
            for c in range(col):
                matrix[0][c] = 0


if __name__ == '__main__':
    testSolution = Solution()

    matrix = [[1, 20, 1, 5, 3, 2]]
    testSolution.setZeroes(matrix)

    print(matrix)
