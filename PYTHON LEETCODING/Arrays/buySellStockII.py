# Solution: https://www.youtube.com/watch?v=3SJ3pUkPQMc
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0

        LENGTH = len(prices)
        buy = prices[0]
        for i in range(1, LENGTH):
            if (prices[i] > prices[i - 1]):
                total_profit += prices[i] - prices[i-1]
        return total_profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4, 100]

    test = Solution()
    print(test.maxProfit(prices))