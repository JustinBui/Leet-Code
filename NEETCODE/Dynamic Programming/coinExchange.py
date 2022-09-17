class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        cache = [None] * (amount + 1)
        cache[0] = []
        
        for i in range(1, len(cache)):
            for denom in coins:
                if i >= denom:
                    if cache[i - denom] != None:
                        candidate = cache[i - denom][:] + [denom]
                        
                        if cache[i] == None or len(candidate) < len(cache[i]):
                            cache[i] = candidate
        
        return len(cache[amount]) if cache[amount] else -1

if __name__ == '__main__':
    obj = Solution()

    c = [2]
    a = 3

    print(obj.coinChange(c, a))