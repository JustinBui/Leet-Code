class Solution:
    def minSwaps(self, s: str) -> int:
        extra_close, max_extra_close = 0, 0

        for i in s:
            if i == ']':
                extra_close += 1
            elif i == '[':
                extra_close -= 1
            
            max_extra_close = max(max_extra_close, extra_close)
        
        return (max_extra_close + 1) // 2