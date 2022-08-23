#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

class Solution
{
private:
    // All the numbers and corresponding letters it maps to
    map<char, string> data = {
        pair<char, string>('2', "abc"),
        pair<char, string>('3', "def"),
        pair<char, string>('4', "ghi"),
        pair<char, string>('5', "jkl"),
        pair<char, string>('6', "mno"),
        pair<char, string>('7', "pqrs"),
        pair<char, string>('8', "tuv"),
        pair<char, string>('9', "wxyz")};
    vector<string> result;

public:
    void backtrack(int i, string currString, string digits)
    {                                           // Recursive function
        if (currString.size() == digits.size()) // went over all of digits string
        {
            result.push_back(currString);
            return;
        }
        for (auto c : data[digits[i]])
        {
            backtrack(i + 1, currString + c, digits);
        }
    }

    vector<string> letterCombinations(string digits)
    {
        int index = 0;

        if (!digits.empty())
            backtrack(index, "", digits);

        return result;
    }
};

int main()
{
    Solution mySol;
    vector<string> answer = mySol.letterCombinations("");

    for (auto it : answer)
    {
        cout << "[ ";
        for (auto c : it)
        {
            cout << c << " ";
        }
        cout << " ]" << endl;
    }
    return 0;
}
