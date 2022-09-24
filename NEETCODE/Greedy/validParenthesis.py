class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            
            else: # '*' (Wildcard character)
                leftMin -= 1 # If wildcard character was a ')'
                leftMax += 1 # If wildcard character was a '('
                
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
                    
        return leftMin == 0