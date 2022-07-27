class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        legend = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c == '(':
                stack.append(legend[c])
            elif c == '{':
                stack.append(legend[c])
            elif c == '[':
                stack.append(legend[c])
            else:  # ')', '}', ']'
                if (len(stack) == 0) or (stack[-1] != c):
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()

    s = "}}}]]"

    print(sol.isValid(s))
