#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> twoSum(vector<int> &, int);

int main()
{
    vector<int> numbers = {-1, 0};
    int target = -1;

    vector<int> result = twoSum(numbers, target);
    for (int i = 0; i < result.size(); ++i)
    {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}

vector<int> twoSum(vector<int> &numbers, int target)
{
    vector<int> result = {};
    int l = 0, r = numbers.size() - 1;
    while (l < r)
    {
        if (numbers[l] + numbers[r] == target)
        {
            result.push_back(l + 1);
            result.push_back(r + 1);
            break;
        }
        else if (numbers[l] + numbers[r] > target)
        {
            r--;
            while (r != numbers.size() - 1 && numbers[r] == numbers[r + 1])
                r--;
        }
        else if (numbers[l] + numbers[r] < target)
        {
            l++;
            while (l != 0 && numbers[l] == numbers[l - 1])
                l++;
        }
    }

    return result;
}