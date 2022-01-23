class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if (needle == ""):
            return 0

        if (len(haystack) >= len(needle)):
            for h in range(len(haystack)):
                if (haystack[h] == needle[0]):
                    if (h + len(needle) <= len(haystack) and haystack[h:h + len(needle)] == needle):
                        return h
        return -1


haystack = "are"
needle = "are"

test = Solution()
print(test.strStr(haystack, needle))
