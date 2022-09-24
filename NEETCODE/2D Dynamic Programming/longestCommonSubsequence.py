class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        row = len(text1) + 1
        col = len(text2) + 1
        
        T = [[0] * col for i in range(row)]
        
        # for r in range(row):
        #     for c in range(col):
        #             print(T[r][c], end=' ')
        #     print('')
            
        
        for r in range(1, row):
            for c in range(1, col):
                if text1[r - 1] == text2[c - 1]:
                    T[r][c] = T[r - 1][c - 1] + 1
                else:
                    T[r][c] = max(T[r - 1][c], T[r][c - 1])
        
        for r in range(row):
            for c in range(col):
                print(T[r][c], end=' ')
            print('')

        return T[row - 1][col - 1]

if __name__ == '__main__':
    obj = Solution()
    text1 = "abcba"
    text2 = "abcbcba"
    print(obj.longestCommonSubsequence(text1, text2))