class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for t in tokens:
            if t in operators:
                op1 = int(stack[-2])
                op2 = int(stack[-1])

                if t == '+':
                    res = op1 + op2
                elif t == '-':
                    res = op1 - op2
                elif t == '/':
                    res = op1 // op2
                elif t == '*':
                    res = op1 * op2

                stack.pop()
                stack.pop()
                stack.append(res)

            else:  # if t is a numerical value
                stack.append(t)

        return stack[0]


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]

    sol = Solution()
    print(sol.evalRPN(tokens))

    # print(f'TEST: {int(6 / -132)}')
