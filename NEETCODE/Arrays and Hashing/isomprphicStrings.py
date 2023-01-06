class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        map_st = dict()
        map_ts = dict()

        for i in range(n):
            if (s[i] in map_st and map_st[s[i]] != t[i]) or (t[i] in map_ts and map_ts[t[i]] != s[i]):
                return False
            map_st[s[i]] = t[i]
            map_ts[t[i]] = s[i]

        return True

if __name__ == '__main__':
    entity = Solution()

    s, t = 'paper', 'title'
    print(entity.isIsomorphic(s, t))