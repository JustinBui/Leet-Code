class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        letters = []
        legend = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 0:
            return res

        def backtrack(i):
            if i == len(digits):
                res.append(''.join(letters))
                return

            # for j in range(i, len(digits)):
            for l in legend[digits[i]]:
                letters.append(l)
                backtrack(i + 1)
                letters.pop()

        backtrack(0)

        return res


if __name__ == '__main__':
    digits = "275"

    obj = Solution()

    print(obj.letterCombinations(digits))
