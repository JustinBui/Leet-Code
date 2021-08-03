// Solution: https://www.youtube.com/watch?v=H9bfqozjoqs (NeetCode)
//           https://www.youtube.com/watch?v=jgiZlGzXMBw (BackToSWE)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{

public:
    // Bottom up approach
    int coinChange(vector<int> &coins, int amount)
    {
        vector<int> allAmounts(amount + 1, amount + 1);
        allAmounts[0] = 0; // If we start at 0 amount, then there are 0 ways to make the coins sum up

        for (int a = 1; a < allAmounts.size(); ++a)
        {
            for (int c = 0; c < coins.size(); ++c)
            {
                if (a - coins[c] >= 0)
                    allAmounts[a] = min(allAmounts[a], 1 + allAmounts[a - coins[c]]);
            }
        }

        if (allAmounts[amount] == amount + 1)
            return -1;
        else
            return allAmounts[amount];
    }
};

int main()
{
    Solution mySol;

    vector<int> c = {1, 4, 5};
    int a = 7;

    cout << mySol.coinChange(c, a) << endl;
    return 0;
}
