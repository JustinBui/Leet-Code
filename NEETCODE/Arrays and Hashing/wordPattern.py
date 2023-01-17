class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False
        
        p_dict = dict()
        s_dict = dict()

        for i in range(len(s)):
            if (pattern[i] in p_dict and p_dict[pattern[i]] != s[i]) or (s[i] in s_dict and s_dict[s[i]] != pattern[i]):
                return False

            p_dict[pattern[i]] = s[i]
            s_dict[s[i]] = pattern[i]
        
        return True