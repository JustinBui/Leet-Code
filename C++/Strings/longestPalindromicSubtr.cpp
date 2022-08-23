// Solution: https://www.youtube.com/watch?v=XYQecbcd6_c

#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        string sol = "";
        int longestLength = 0;

        for (int i = 0; i < s.size(); ++i)
        {
            int l = i, r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) // While still in bound and a palindrome
            {
                int currLength = (r - l) + 1;

                if (currLength > longestLength)
                {
                    sol = s.substr(l, currLength);
                    longestLength = currLength;
                }

                l--;
                r++;
            }

            l = i, r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r])
            {
                int currLength = (r - l) + 1;

                if (currLength > longestLength)
                {
                    sol = s.substr(l, currLength);
                    longestLength = currLength;
                }

                l--;
                r++;
            }
        }

        return sol;
    }
};

int main()
{
    Solution mySol;

    string res = mySol.longestPalindrome("babad");
    cout << res << endl;

    return 0;
}
