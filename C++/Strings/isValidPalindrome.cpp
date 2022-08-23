#include <iostream>
#include <string>
#include <cctype>

using namespace std;

// race:::::::car
bool isPalindrome(string);

int main()
{
    string param = " ";
    cout << isPalindrome(param) << endl;
    return 0;
}

bool isPalindrome(string s)
{
    int l = 0, r = s.size() - 1;

    while (l < r)
    {
        while (l < r && !isalnum(s[l]))
            l++;

        while (l < r && !isalnum(s[r]))
            r--;

        if (l < r && tolower(s[l++]) != tolower(s[r--]))
            return false;
    }

    return true;
}