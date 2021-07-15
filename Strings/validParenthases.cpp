#include <iostream>
#include <string>
#include <stack>
#include <map>

using namespace std;

bool isValid(string);

int main()
{
    cout << isValid("]") << endl;

    return 0;
}

bool isValid(string s)
{
    stack<char> openingParentheses;
    map<char, char> parenthasesMap =
        {
            pair<char, char>('(', ')'),
            pair<char, char>('{', '}'),
            pair<char, char>('[', ']')};

    for (string::iterator it = s.begin(); it != s.end(); ++it)
    {
        // Opening parenthases that still need to be closed
        map<char, char>::iterator got = parenthasesMap.find(*it);
        if (got != parenthasesMap.end()) // Open parenthases found
            openingParentheses.push(*it);
        // Closed parenthases found
        else if (got == parenthasesMap.end())
        {
            if (openingParentheses.empty() || *it != parenthasesMap[openingParentheses.top()]) // Not corresponding closed parenthases
                return false;
            else if (*it == parenthasesMap[openingParentheses.top()]) // Corresponding closed parenthases
                openingParentheses.pop();
        }
    }

    if (!openingParentheses.empty())
        return false;

    return true;
}