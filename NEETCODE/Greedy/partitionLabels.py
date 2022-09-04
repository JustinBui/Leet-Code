class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        
        last_indices = {}
        for i in range(len(s)):
            last_indices[s[i]] = i
        
        size = 0
        strech = 0

        for i in range(len(s)):
            strech = max(strech, last_indices[s[i]])
            size += 1
            
            if i == strech:
                res.append(size)
                size = 0
                
        return res