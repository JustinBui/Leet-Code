class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        cache = [None] * (amount + 1)  # Creating array of amount + 1 items
        cache[0] = []

        for i in range(1, amount + 1):
            for coin in coins:
                if (i >= coin and cache[i - coin] != None):
                    candidate = cache[i - coin] + [coin]
                    if (cache[i] == None or len(candidate) < len(cache[i])):
                        cache[i] = candidate

        if (cache[amount] == None):
            return -1
        else:
            return len(cache[amount])


if __name__ == "__main__":
    mySol = Solution()

    coins = [1]
    amount = 0

    print(mySol.coinChange(coins, amount))
