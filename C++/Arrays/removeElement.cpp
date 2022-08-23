#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int valsFound = 0;
        int initialSize = nums.size();
        for (vector<int>::iterator it = nums.begin(); it != nums.end();)
        {
            if (*it == val)
            {
                valsFound++;
                nums.erase(it);
            }
            else
                ++it;
        }

        return initialSize - valsFound; // k
    }
};

int main()
{
    vector<int> numbers = {0, 1, 2, 2, 3, 0, 4, 2};
    int val = 2;

    Solution mySol;

    cout << "k = " << mySol.removeElement(numbers, val) << endl;

    cout << "[";
    for (int i = 0; i < numbers.size(); ++i)
    {
        cout << numbers[i] << " ";
    }
    cout << "]" << endl;

    return 0;
}