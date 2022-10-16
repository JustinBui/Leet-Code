class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        s_ptr = 0
        
        for t_ptr in range(len(t)):
            if s_ptr == len(s):
                break
            
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
        
        # If s_ptr going out of bound, therefore we checked off every
        # matching character s in the same sequence as t (therefore s is subsequence)
        return True if s_ptr == len(s) else False