#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int k = nums.size();

        if (!nums.empty())
        {
            int newTerm = nums[0];
            for (auto it = nums.begin() + 1; it != nums.end();)
            {
                if (newTerm == *it) // Duplicates detected
                {
                    nums.erase(it);
                    k--;
                }
                else
                {
                    newTerm = *it; // Updating newTerm
                    it++;
                }
            }
        }

        return k;
    }
};

int main()
{
    Solution entity;

    vector<int> numbers = {};
    cout << numbers.size() << endl;

    cout << entity.removeDuplicates(numbers) << endl;

    cout << "[";
    for (int i = 0; i < numbers.size(); ++i)
        cout << numbers[i] << ", ";
    cout << "]";

    return 0;
}