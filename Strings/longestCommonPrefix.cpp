#include <iostream>
#include <string>
#include <vector>

using namespace std;

string longestCommonPrefix(vector<string> &);

int main()
{
    vector<string> strs = {"flower", "flow", "flight"};
    vector<string> strs2 = {"123333", "123333racecar", "123333car"};
    vector<string> strs3 = {"sefsefefa", "33"};

    cout << longestCommonPrefix(strs3) << endl;

    return 0;
}

string longestCommonPrefix(vector<string> &strs)
{
    string prefix = "";
    int charIndex = 0;
    bool similarity = true;

    while (similarity)
    {
        string::iterator it = strs[0].begin() + charIndex; // Using first element as reference
        char referenceLetter = *it;

        for (int i = 0; i < strs.size(); ++i)
        {
            string::iterator it2 = strs[i].begin() + charIndex;
            char currentLetter = *it2;

            if (it2 == strs[i].end() || referenceLetter != currentLetter)
            {
                similarity = false;
                break;
            }
        }

        if (similarity)
            prefix.push_back(referenceLetter);

        charIndex++;
    }

    return prefix;
}