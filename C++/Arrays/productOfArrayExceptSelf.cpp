// Solution: https://www.youtube.com/watch?v=bNvIQI2wAjk

#include <iostream>
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int> &);

int main()
{
    vector<int> input = {1, 2, 3, 4};
    vector<int> output = productExceptSelf(input);

    for (auto it = output.begin(); it != output.end(); ++it)
        cout << *it << " ";
    cout << endl;

    return 0;
}

vector<int> productExceptSelf(vector<int> &nums)
{
    vector<int> sol;
    int pre = 1, post = 1;

    // Getting all prefixes
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); ++it)
    {
        if (it != nums.begin())
            pre *= *(it - 1);

        sol.push_back(pre);
    }

    for (int i = nums.size() - 1; i >= 0; --i)
    {
        if (i != nums.size() - 1)
            post *= nums[i + 1];
        sol[i] *= post;
    }

    return sol;
}
