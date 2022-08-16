class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i: int):
            if i == len(s):
                res.append(part[:])
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    # Going down the tree recursively to append partitions into our part[] array
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)

        return res

# def partition(word):
#     res = []
#     part = []

#     def dfs(i):
#         if i == len(word):
#             res.append(part[:])
#             return

#         for j in range(i, len(word)):
#             part.append(word[i:j+1])
#             dfs(j+1)
#             part.pop()

#     dfs(0)

#     return res


print(partition('abcd'))
