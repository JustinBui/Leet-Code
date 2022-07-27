class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0

        while r < len(s2):
            # Not a valid substring
            if (r - l + 1) < len(s1):
                r += 1
            else:
                substr_list = list(s1)
                it = r
                while (it >= l) and (s2[it] in substr_list):
                    substr_list.remove(s2[it])
                    it -= 1

                if len(substr_list) == 0:
                    return True
                else:
                    l = it + 1
                    r = l

        return False


if __name__ == '__main__':
    s1 = "aeiou"
    s2 = "uaioee"

    sol = Solution()
    print(sol.checkInclusion(s1, s2))
