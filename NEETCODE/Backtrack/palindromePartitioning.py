# class Solution:
#     def partition(self, s: str) -> list[list[str]]:
#         res = []
#         part = []

#         def backtrack(s: str):
#             if not s:
#                 res.append(part[:])
#                 return

#             for i in range(len(s)):
#                 part.append(s[0:i+1])
#                 self.partition(s[i+1:])

#         backtrack(s)

#         return res


# obj = Solution()

# print(obj.partition('abcd'))

def partition(word):
    res = []
    part = []

    def dfs(i):
        if i == len(word):
            res.append(part[:])
            return

        for j in range(i, len(word)):
            part.append(word[i:j+1])
            dfs(j+1)
            part.pop()

    dfs(0)

    return res


print(partition('abcd'))
