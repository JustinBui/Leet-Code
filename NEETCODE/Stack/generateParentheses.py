# SOLUTION FROM NEETCODE

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        all_parentheses_result = []
        call_stack = []

        def backTrack(openParen, closedParen):
            # -------------- BASE CASE (Used to backtrack) --------------
            if openParen == closedParen == n:
                all_parentheses_result.append(''.join(call_stack))
                return

            # -------------------- RECURSIVE CASE --------------------
            if openParen < n:
                call_stack.append('(')
                backTrack(openParen + 1, closedParen)
                call_stack.pop()
            if closedParen < openParen:
                call_stack.append(')')
                backTrack(openParen, closedParen + 1)
                call_stack.pop()

        backTrack(0, 0)
        return all_parentheses_result


if __name__ == '__main__':
    obj = Solution()
    print(obj.generateParenthesis(3))
