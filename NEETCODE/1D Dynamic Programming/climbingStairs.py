class Solution:
    def climbStairs(self, n: int) -> int:
        T = [0] * max(3, n + 1)
        T[1], T[2] = 1, 2
        
        for i in range(3, n + 1):
            T[i] = T[i - 1] + T[i - 2]
        
        return T[n]
        
        
if __name__ == '__main__':
    s = Solution()

    print(s.climbStairs(4))