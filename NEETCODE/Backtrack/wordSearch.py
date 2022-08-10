# O(n * m * 4^n)
from importlib.machinery import PathFinder


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()

        def pathfind_dfs(r, c, i) -> bool:
            # --------------- BASE CASES ---------------
            if len(word) == i:
                return True  # We found the correct word!

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                # Out of bounds
                return False
            if word[i] != board[r][c]:
                # Incorrect match, just end the recursion from here
                return False
            if i > len(word):
                # Path length over exceeded length of our word
                return False
            if (r, c) in path:
                # We've already visited this path before, which we CANNOT do
                return False

            # --------------- RECURSIVE CASES ---------------
            path.add((r, c))
            result = pathfind_dfs(r + 1, c, i + 1) or pathfind_dfs(r - 1, c, i +
                                                                   1) or pathfind_dfs(r, c + 1, i + 1) or pathfind_dfs(r, c - 1, i + 1)
            path.pop()  # remove((r, c))

            return result

        for r in range(ROWS):
            for c in range(COLS):
                if pathfind_dfs(r, c, 0):
                    return True  # If in any case it is true, automatically RETURN TRUE

        # None of the cases during the pathfinding backtrack are true, RETURN FALSE
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"

    obj = Solution()
    print(obj.exist(board, word))
