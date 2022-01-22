# Solution: https://www.youtube.com/watch?v=TjFXEUCMqI8
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        record_cols = defaultdict(list)
        record_rows = defaultdict(list)
        record_squares = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if (board[r][c] != "."):
                    if (board[r][c] in record_cols[c] or
                        board[r][c] in record_rows[r] or
                            board[r][c] in record_squares[(r // 3, c // 3)]):
                        return False
                    else:
                        record_rows[r].append(board[r][c])
                        record_cols[c].append(board[r][c])
                        record_squares[(r // 3, c // 3)].append(board[r][c])

        return True


if __name__ == "__main__":
    # sodoku_board = [["5", "3", ".", ".", "7", "5", ".", ".", "."],
    #                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    sodoku_board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
                    [".", "4", ".", "3", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                    [".", ".", "2", ".", "7", ".", ".", ".", "."],
                    [".", "1", "5", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", "2", ".", ".", "."],
                    [".", "2", ".", "9", ".", ".", ".", ".", "."],
                    [".", ".", "4", ".", ".", ".", ".", ".", "."]]

    test = Solution()
    print(test.isValidSudoku(sodoku_board))
