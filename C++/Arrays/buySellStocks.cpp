#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int maxProfit = 0;
        int smallestVal = prices[0];

        for (vector<int>::iterator it = prices.begin(); it != prices.end(); it++)
        {
            if (*it < smallestVal)
            {
                smallestVal = *it;
            }
            else if (*it - smallestVal > maxProfit)
            {
                maxProfit = *it - smallestVal;
            }
        }

        return maxProfit;
    }
};

int main()
{
    vector<int> prices = {2, 4, 1};
    Solution test;

    cout << test.maxProfit(prices) << endl;

    return 0;
}

// {3, 99, ... 98, 100}