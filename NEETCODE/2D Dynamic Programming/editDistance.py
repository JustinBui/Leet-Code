class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row, col = len(word1) + 1, len(word2) + 1
        T = [[0] * col for i in range(row)]
        
        # Filling the outside of matrix with increasing numbers
        # (First row, and first columns only)
        for c in range(1, col):
            T[0][c] = c
        for r in range(1, row):
            T[r][0] = r
        
        # Looping through the matrix at the 1th positions of rows and columns
        # to analyze how many edit operations are needed for each entry of matrix
        for r in range(1, row):
            for c in range(1, col):
                if word1[r - 1] != word2[c - 1]:
                    T[r][c] = min(T[r - 1][c - 1], T[r][c - 1], T[r - 1][c]) + 1
                else: # If word1[r - 1] == word2[c - 1]
                    T[r][c] = T[r - 1][c - 1]
        
        return T[row-1][col-1] # Last item of matrix is the final value calculated

if __name__ == '__main__':
    obj = Solution()

    w1 = 'a'
    w2 = 'j'
    print(obj.minDistance(w1, w2))