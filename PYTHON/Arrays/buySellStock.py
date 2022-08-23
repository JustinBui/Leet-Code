class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest_profit = 0
        lowest_profit = prices[0]
        LENGTH = len(prices)

        for i in range(LENGTH):
            if (prices[i] < lowest_profit):
                lowest_profit = prices[i]
            elif (prices[i] - lowest_profit > highest_profit):
                highest_profit = prices[i] - lowest_profit
        
        return highest_profit

if __name__ == '__main__':
    prices = [2,4,1, 100]

    test = Solution()
    print(test.maxProfit(prices))