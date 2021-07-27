#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        string res;
        vector<pair<int, string>> data = {
            pair<int, string>(1000, "M"),
            pair<int, string>(900, "CM"),
            pair<int, string>(500, "D"),
            pair<int, string>(400, "CD"),
            pair<int, string>(100, "C"),
            pair<int, string>(90, "XC"),
            pair<int, string>(50, "L"),
            pair<int, string>(40, "XL"),
            pair<int, string>(10, "X"),
            pair<int, string>(9, "IX"),
            pair<int, string>(5, "V"),
            pair<int, string>(4, "IV"),
            pair<int, string>(1, "I")};

        for (auto it = data.begin(); it != data.end(); ++it)
        {
            int timesModed = num / it->first;
            for (int i = 0; i < timesModed; ++i)
            {
                num %= it->first;
                res += it->second;
            }
        }

        return res;
    }
};

int main()
{
    Solution mySol;

    string answer = mySol.intToRoman(1994);
    cout << answer << endl;

    return 0;
}