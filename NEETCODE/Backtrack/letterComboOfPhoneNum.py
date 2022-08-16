class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = ''
        legend = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(i):
            if i == len(digits):
                res.append(letters[:])
                return

            for j in range(len(legend[digits[i]])):
                letters.append(legend[digits[i]])
                backtrack(i + 1)
                letters.pop()

        return res
