class Solution(object):
    def generate(self, numRows):
        T = [[]] * (numRows)
        
        T[0] = [1]
        
        for i in range(1, numRows):
            T[i] = [1, 1]
            
            for j in range(0, len(T[i-1])-1):
                index_append = 1
                T[i].insert(index_append, T[i-1][j] + T[i-1][j+1])
                index_append += 1
                
        
        return T
        