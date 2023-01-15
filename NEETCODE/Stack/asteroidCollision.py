class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ast_stack = []

        for a in asteroids:
            ast_stack.append(a)

            while len(ast_stack) >= 2:
                first, second = len(ast_stack) - 2, len(ast_stack) - 1

                if ast_stack[first] > 0 and ast_stack[second] < 0: # If asteroids are colliding
                    if abs(ast_stack[first]) > abs(ast_stack[second]):
                        # First asteroid is bigger, so second gets eliminated
                        ast_stack.pop(second)
                    elif abs(ast_stack[first]) < abs(ast_stack[second]):
                        # Second asteroid is bigger, so first gets eliminated
                        ast_stack.pop(first)
                    else:
                        # Both are same size, so both are eliminated
                        ast_stack.pop()
                        ast_stack.pop()
                else:
                    break

        return ast_stack

if __name__ == '__main__':
    entity = Solution()

    a = [10,2,-5]
    print(entity.asteroidCollision(a))